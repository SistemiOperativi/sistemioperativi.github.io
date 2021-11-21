.. role:: raw-html(raw)
   :format: html

FEW - Fork-Exit-Wait 
====================

.. code-block:: c
    :linenos:
    
    #include <unistd.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <sys/wait.h>
    
    int main(){
        int res, status;
        printf("I'm a process and I'm going to create a child\n");
        res = fork();
        if(res < 0) printf("I cannot create a child");
        else if(res == 0){
            sleep(5);
            printf("I'm the child!\n");
            exit(1);
        }
        else{
            printf("I'm now a parent and I'll wait for my child to die...\n");
            wait(&status);
            printf("My child has invoked exit(%d)\n", WEXITSTATUS(status));
            printf("My child is dead, so it's my time to die\n");
        }
        exit(0);
    }

Fork-Exit-Wait 
(:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/few/few.c">FEW</a>
<a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/few/few.c"></a>`) 
è un semplice programma C per:

1. Creare un processo tramite :posix:`fork <fork>`. 
2. Attendere la terminazione del processo appena creato tramite :posix:`wait <wait>`.
3. Terminare il processo corrente utilizzando :posix:`exit <exit>`.

Il main thread esegue la stampa di riga 8 e successivamente invoca la :posix:`fork <fork>` per creare un processo child.

.. code-block:: c
    :lineno-start: 8

        printf("I'm a process and I'm going to create a child\n");
        res = fork();

Se la :posix:`fork <fork>` fallisce (:code:`res == -1`), il processo principale termina.
Altrimenti, entrambi i processi eseguono a partire dalla terminazione della :posix:`fork <fork>`.

Per differenziare il flusso di esecuzione tra il processo parent ed il processo child occorre analizzare 
il risultato della :posix:`fork <fork>`.
Il processo child legge :code:`res == 0`, mentre il processo parent :code:`res != 0` (più precisamente 
:code:`res` contiene il pid del processo child).
A questo punto il child esegue:

.. code-block:: c
    :lineno-start: 12

            sleep(5);
            printf("I'm the child!\n");
            exit(1);

ossia va in stato di sleep per 5 secondi, esegue una stampa e termina con codice di terminazione 1 invocando la syscall :posix:`exit <exit>`.

Il parent esegue:

.. code-block:: c
    :lineno-start: 17

            printf("I'm now a parent and I'll wait for my child to die...\n");
            wait(&status);
            printf("My child has invoked exit(%d)\n", WEXITSTATUS(status));
            printf("My child is dead, so it's my time to die\n");

Nello specifico attende la terminazione di uno generico thread child tramite la system call :posix:`wait <wait>`.
Grazie a questa chiamata, può inoltre ottenere il codice di terminazione dalla variabile :code:`status` 
grazie alla macro :code:`WEXITSTATUS` (il codice è memorizzato nel secondo byte di :code:`status`).


Riferimenti
"""""""""""

* [:ref:`t3 <books>`] Sezione 1.2, 3.1
* :posix:`fork <fork>`
* :posix:`exit <exit>`
* :posix:`wait <wait>`
