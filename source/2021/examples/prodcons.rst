.. role:: raw-html(raw)
   :format: html

ProdCons
==========


:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/prod_cons">ProdCons</a>
<a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/prod_cons"></a>`
è un programma C il cui obiettivo è mostrare l'utilizzo di semplici servizi per la gestione di file.

.. code-block:: c
    :linenos:

    #ifndef __PROD_CONS__
    #define __PROD_CONS__

    #define SHARED_SIZE 4096
    #define SHARED_NAME "prod_cons_shm"
    #define LONG_SHARED_NAME "/dev/shm/"SHARED_NAME
    #define MSG_SIZE 255
    #define MSG_SIZE_RAW 256
    #define log(...) do{printf("[%d]:", getpid()); printf(__VA_ARGS__);}while(0)

    #include <pthread.h>

    typedef struct __shared_data{
        pthread_barrier_t barrier;
        pthread_mutex_t mutex;
        void *prod_base_addr;
        pid_t prod_pid;
        pid_t cons_pid;
        char message[256];
    }shared_data_t;

    #endif

.. code-block:: c
    :linenos:

    #include <sys/mman.h>
    #include <sys/stat.h>        /* For mode constants */
    #include <fcntl.h>           /* For O_* constants */
    #include <unistd.h>          /* For truncate */
    #include <stdio.h>           /* For printf */
    #include <stdlib.h>          /* For exit */

    #include "prod_cons.h"



    int main(int argc, char *argv[]){
        shared_data_t *shared_data;    
        pthread_barrierattr_t pthread_barrierattr;
        pthread_mutexattr_t   pthread_mutexattr;
        int res;
        pid_t pid = getpid();

        int fd = shm_open(SHARED_NAME, O_CREAT | O_EXCL | O_RDWR, 0666);
        if(fd == -1) {
            log("The shared memory already exists...Probably there is another producer...exit\n");
            goto fail_exit;
        }
        
        res = ftruncate(fd, SHARED_SIZE); 
        if(res == -1) {
            log("I cannot allocate enough memory...exit\n");
            goto abort;
        }
        
        shared_data = mmap(NULL, SHARED_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
        if(shared_data == MAP_FAILED) {
            log("I cannot map memory...exit\n");
            goto abort;
        }

        close(fd);

        pthread_barrierattr_setpshared(&pthread_barrierattr, PTHREAD_PROCESS_SHARED );
        pthread_barrier_init(&shared_data->barrier, &pthread_barrierattr, 2);

        pthread_mutexattr_settype(&pthread_mutexattr, PTHREAD_MUTEX_DEFAULT);
        pthread_mutexattr_setpshared(&pthread_mutexattr,  PTHREAD_PROCESS_SHARED);
        pthread_mutex_init(&shared_data->mutex, &pthread_mutexattr);

        log("I'll WAIT for a process at %p\n", shared_data);
        shared_data->prod_pid = pid;
        shared_data->prod_base_addr = shared_data;
        shared_data->message[MSG_SIZE] = '\0';
        pthread_mutex_lock(&shared_data->mutex);
        pthread_barrier_wait(&shared_data->barrier);
        log("Process %d arrived\n", shared_data->cons_pid);


        log("I'll produce data...\n");
        sprintf(shared_data->message, "Nice to meet you");
        log("Done\n");

        pthread_mutex_unlock(&shared_data->mutex);

        exit(0);

    abort:
        shm_unlink(SHARED_NAME);
        close(fd);
    fail_exit:
        exit(1);


    }



.. code-block:: c
    :linenos:
    
    #include <sys/mman.h>
    #include <sys/stat.h>        /* For mode constants */
    #include <fcntl.h>           /* For O_* constants */
    #include <unistd.h>          /* For truncate */
    #include <stdio.h>           /* For printf */
    #include <stdlib.h>          /* For exit */

    #include "prod_cons.h"



    int main(int argc, char *argv[]){
        shared_data_t *shared_data;
        pid_t pid = getpid();


        int fd = shm_open(SHARED_NAME, O_RDWR, 0666);
        if(fd == -1) {log("shared mem not initialized\n");exit(1);}
        shared_data = mmap(NULL, SHARED_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

        if(shared_data == MAP_FAILED) {
            log("I cannot map memory...exit\n");
            close(fd);
            exit(1);
        }

        log("shared_data cons address %p\n", shared_data);
        log("shared_data prod address %p\n", shared_data->prod_base_addr);
        close(fd);  

        log("I'll JOIN for a process at %p\n", shared_data);
        shared_data->cons_pid = pid;
        pthread_barrier_wait(&shared_data->barrier);
        log("Joined. prod pid %d:\n", shared_data->prod_pid);

        pthread_mutex_lock(&shared_data->mutex);    
        log("I'll consume data...\n");
        log("Message: '%s'\n", shared_data->message);
        log("Done\n");

        pthread_mutex_unlock(&shared_data->mutex);

        shm_unlink(SHARED_NAME);
    }





Riferimenti
"""""""""""

* :posix:`open <open>`
* :posix:`close <close>`
* :posix:`dup <dup>`
* :posix:`exec <exec>`






