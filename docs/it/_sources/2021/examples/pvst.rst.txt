.. role:: raw-html(raw)
   :format: html


PVST - Processi vs Thread
=========================

.. code-block:: c
    :linenos:

    #include <unistd.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <sys/wait.h>

    #include <pthread.h>

    #define INIT_VALUE 0
    #define PARENT_VAL 1
    #define TCHILD_VAL 2
    #define PCHILD_VAL 3

    volatile int global_var = INIT_VALUE;

    void* child_func(void *par){
        *((int*)par) = 1;
        global_var = TCHILD_VAL;
        printf("I'm the child and I wrote the global var: %d\n", global_var);
        pthread_exit(par);
    }

    int main(){
        pthread_t ctid;
        int res, *status;
        printf("I'm a thread. "
                   "I'm going to create another thread\n");
        res = pthread_create(&ctid, NULL, child_func, status);
        global_var = PARENT_VAL;
        if(res != 0) printf("I cannot create a child");
        else{
            printf("I'm now a parent thread. "
                           "I'll wait for my child thread %lu to die...\n", ctid);
            pthread_join(ctid, (void*)&status);
            printf("My child has invoked %d\n",*status);
        }
        printf("My child is dead, so it's my time to die. Global var: %d\n", global_var);
        global_var = PARENT_VAL;
        res = fork();
        if(res == -1) exit(1);
        if(res == 0){
            global_var = PCHILD_VAL;
            printf("Child Global var: %d\n", global_var);
            exit(0);
        }
        wait(&res);
        printf("Parent Global var: %d\n", global_var);
        return 0;
    }


Processi vs Thread 
(:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/pvst/pvst.c">PVST</a>
<a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/pvst/pvst.c"></a>`) 
è un programma C il cui scopo è quello di evidenziare differenze basilari tra processi e thread.

Il programma è diviso in due sezioni:

1. il main thread crea un thread child secondo lo schema proposto in :doc:`PFEW <pfew>`. Entrambi i thread scrivono sulla variabile globale :code:`global_var` e successivamente ne stampano il valore su standard output.
2. il main thread crea un processo child secondo lo schema proposto in :doc:`FEW <few>`. Entrambi i processi scrivono sulla variabile globale :code:`global_var` e successivamente ne stampano il valore su standard output.

La variabile :code:`global_var` viene stampata 4 volte, rispettivamente

.. code-block:: c
    :lineno-start: 18

    printf("I'm the child and I wrote the global var: %d\n", global_var);


.. code-block:: c
    :lineno-start: 36

    printf("My child is dead, so it's my time to die. Global var: %d\n", global_var);


.. code-block:: c
    :lineno-start: 42

        printf("Child Global var: %d\n", global_var);


.. code-block:: c
    :lineno-start: 46

    printf("Parent Global var: %d\n", global_var);



.. question_note::

    Cosa stampano le righe 18, 36, 42 e 46?


