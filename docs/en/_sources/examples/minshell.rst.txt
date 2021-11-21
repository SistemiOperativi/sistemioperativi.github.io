.. role:: raw-html(raw)
   :format: html

MinShell - le funzioni exec
===========================

.. code-block:: c
    :linenos:
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include <sys/wait.h>

    int main() {
       char comando[256];
       pid_t pid; int status;

       while(1) 
       {
         printf("Digitare un comando: ");
         int res = scanf("%s",comando);
         if(res == EOF) continue;
         pid = fork();
         if ( pid == -1 ) {
           printf("Errore nella fork.\n");
           exit(1);
         }
         if ( pid == 0 )
            execlp(comando, comando, NULL);
         else wait(&status);
       }
       return 0;
    }

Una shell è una interfaccia testuale per il sistema operativo attraverso la quale è possibile eseguire comandi 
e programmi.
Ogni qual volta si lancia un programma X tramite shell, quest'ultima crea un nuovo processo la cui immagine è quella
del programma X.

:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/minshell/minshell.c">MinShell</a>
<a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/minshell/minshell.c"></a>`
è un programma C che emula questo comportamento.
Il principio di funzionamento è analogo a quello di :doc:`FEW <few>`.

Tuttavia, ricorrendo alla sola syscall fork, :doc:`FEW <few>`: può solo creare processi con il medesimo programma del processo parent.
Per superare questo limite, è possibile ricorrere alla famiglia di funzioni :posix:`exec <exec>`. 
Grazie ad una syscall di tipo :posix:`exec <exec>` è possibile sostituire completamente l'immagine del processo che invoca la 
system call con quella di un altro programma. 

Di conseguenza, lo schema di esecuzione di MinShell è il seguente:

* il processo principale crea un processo child tramite :posix:`fork <fork>`
* il processo child invoca una funzione di tipo :posix:`exec <exec>`
* il processo principale attende la sua terminazione tramite :posix:`wait <wait>`

Per sostituire il programma di un'immagine, una funzione :posix:`exec <exec>` ha bisogno:

* individuare l'esatta posizione del programma nel filesystem
* setup dell'ambiente di esecuzione
* eventuali parametri da passare al programma target

A tal scopo la funzione :posix:`execlp <execlp>`:

* considera il primo parametro come il nome dell'eseguibile target, il quale viene cercato nei percorsi definiti nella variabile di ambiente PATH
* eredita l'ambiente dal processo che invoca :posix:`execlp <execlp>`

.. question_note::
    Supponendo di lanciare MinShell da linea di comando, qual è l'ambiente del processo child?

* il secondo e i successivi parametri della funzione :posix:`execlp <execlp>` vengono passati come parametri per l'eseguibile

.. observation_note::
    Tipicamente il primo parametro passato ad un programma è una stringa contenente il nome del programma stesso. L'ultimo parametro è impostato a NULL in quanto da standard POSIX la lista di parametri deve terminare con un puntatore NULL.



Riferimenti
"""""""""""

* :posix:`exec <exec>`






