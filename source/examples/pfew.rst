.. role:: raw-html(raw)
   :format: html

PFEW - FEW basato su posix threads
==================================

.. code-block:: c
    :linenos:
        
    #include <unistd.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <sys/wait.h>

    #include <pthread.h>

    void* child_func(void *par){
      *((int*)par) = 1;
      sleep(5);
      printf("I'm the child!\n");
      pthread_exit(par);
    }

    int main(){
        pthread_t ctid;
        int res, *status_ptr, status_val;
        status_ptr = &status_val;
        printf("I'm a thread. I'm going to create another thread\n");
        res = pthread_create(&ctid, NULL, child_func, &status_val);
        if(res != 0) printf("I cannot create a child");
        else{
            printf("I'm now a parent thread. "
                           "I'll wait for my child %lu thread to die...\n", ctid);
            pthread_join(ctid, (void**)&status_ptr);
            printf("My child has invoked %d\n", *status_ptr);
        }
        printf("My child is dead, so it's my time to die\n");
        return 0;
    }

Pthread FEW
(:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/pfew/pfew.c">PFEW</a>
<a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/pfew/pfew.c"></a>`) 
è un semplice programma C per emulare il comportamento del programma :doc:`FEW <few>`, ma utilizzando i thread al posto di processi.

Di conseguenza PFEW:

1. Creare un thread tramite :posix:`pthread_create <pthread_create>`.

.. observation_note::
    A differenza della :posix:`fork <fork>`, la :posix:`pthread_create <pthread_create>` 
    richiede come terzo parametro la funzione che il thread child deve eseguire. 
    Tale funzione riceve un parametro che corrisponde all'ultimo (quarto) paramentro di invocazione 
    della :posix:`pthread_create <pthread_create>`.
    Il primo parametro invece è un puntatore ad un'area di memoria dove il parent thread può accedere per ottenere
    il :code:`pthread_t`, ossia il thread id, caratteristico del thread child.
    Infine, il secondo parametro è un puntatore ad una struttura dati di tipo :code:`pthread_attr_t`, opportunamente inizializzata da
    un'invocazione a :posix:`pthread_attr_init <pthread_attr_init>`, attraverso la quale è possibile
    configurare alcune proprietà del thread child, tra cui:

    * dimensione minima e posizione dello stack per il thread child;
    * scheduling policy e priorità del thread child.



2. Attendere la terminazione del thread child tramite :posix:`pthread_join <pthread_join>`.

.. observation_note::
    A differenza di quanto accade per i processi con la funzione :posix:`wait <wait>`, per i posix thread
    non esiste una funzione per aspettare un generico thread child. La funzione :posix:`pthread_join <pthread_join>`
    infatti richiede l'id del thread da attendere come primo paramentro. Il secondo parametro invece è utilizzato per
    ricevere un payload generato dal thread child atteso. Nel caso dei processi, un comportamento simile è ottenibile
    grazie alla funzione :posix:`waitpid <waitpid>`. 

3. Il thread child termina con una :posix:`pthread_exit <pthread_exit>`.



Riferimenti
"""""""""""

* :posix:`pthread_create <pthread_create>`
* :posix:`pthread_attr_init <pthread_attr_init>`
* :linux:`pthread_attr_init <pthread_attr_init>`
* :posix:`pthread_join <pthread_join>`
* :posix:`waitpid <waitpid>`
* :posix:`pthread_exit <pthread_exit>`