.. role:: raw-html(raw)
   :format: html

Dup
==========


:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/dup/dup.c">Dup</a>
<a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/dup/dup.c"></a>`
è un programma C il cui obiettivo è mostrare l'utilizzo di semplici servizi per la gestione di file.

.. code-block:: c
    :linenos:
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <fcntl.h>
    #include <unistd.h>

    #define FILE_NAME "log.txt"
    #define STDOUT 1

    #define abort(msg) do{printf(msg);exit(1);}while(0)


    int main() {
        int ofd;

        /* opend output file and check errors */
        ofd=open(FILE_NAME,O_WRONLY|O_CREAT|O_TRUNC,0660); 
        if (ofd == -1) abort("output creation error\n");

        close(STDOUT);  /* close standard output */
        ofd = dup(ofd); /* duplicate file descriptor */
        if (ofd == -1) abort("dup failed\n");

        execlp("ls","ls",NULL); /* run 'ls' */
    }





Riferimenti
"""""""""""

* :posix:`open <open>`
* :posix:`close <close>`
* :posix:`dup <dup>`
* :posix:`exec <exec>`






