:orphan:

.. role:: raw-html(raw)
   :format: html
   
Dup
==========


:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/dup/dup.c">Dup</a>
<a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/dup/dup.c"></a>`
è un programma C il cui obiettivo è mostrare l'utilizzo delle funzione :code:`dup`.

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


In UNIX esistono 3 file descriptor principali:

* 0: standard input;
* 1: standard output;
* 2: standard error.

Secondo lo standard POSIX (:posix:`stdin <stdin>`), questi canali (o stream) sono predefiniti ed aperti implicitamente.
I descrittori referenziano quindi a specifici canali, ma l'associazione può essere cambiata dinamicamente.
Ad esempio, la funzione *dup* associa ad un canale (più precisamente alla file description) già esistente un nuovo descrittore.
Il canale viene individuato a partire dal file descriptor passato come parametro.
Il nuovo descrittore viene invece scelto prendendo il primo disponibile.


Il codice in questione utilizza queste primitive per ridirezionare lo standard output di un eseguibile (in questo caso il comando *ls*) su file regolare.
Lo scopo viene raggiunto in pochi semplici passi:

#. crea ed apre il file destinazione ottenendo il file descriptor *ofd* (riga 16);
#. chiude lo stream di standard output (riga 19), rendendo 1 il primo file descriptor disponibile (0 è impegnato per lo standard input);
#. invoca *dup* passando *ofd* come parametro (riga 20);
#. sostituisce il programma del processo corrente tramite chiamata *exec* (riga 23).

Il comando *ls* stampa su standard output (file descriptor 1), il quale è stato direzionato sul file di log piuttosto che il terminale.

.. observation_note::

    L'ultimo parametro è della *open* è passato in base otto (ogni cifra è compresa tra 0 e 7). Questo è identificato dal fatto che la costante comincia per 0.
    Essendo 8 valori rappresentabili con soli 3 bit, ogni cifra in base 8 corrisponde esattamente a 3 bit.
    Focalizzandoci solo sul literal *0660*, questo è un intero (per l'esattezza un *mode_t*) la cui rappresentazione binaria è:
    
    +-+-+-+-+-+-+-+-+-+
    |User |Group|Other|
    +=+=+=+=+=+=+=+=+=+
    |r|w|x|r|w|x|r|w|x|
    +-+-+-+-+-+-+-+-+-+
    |1|1|0|1|1|0|0|0|0|
    +-+-+-+-+-+-+-+-+-+
    |  6  |  6  |  0  |
    +-+-+-+-+-+-+-+-+-+

    Ulteriori dettagli possono essere trovati a questo link: `Microsoft C docs <https://docs.microsoft.com/cpp/c-language/c-integer-constants>`_.


    .. question_note::
        Come è possibile esprimere i medesimi permessi utilizzando una rappresentazione decimale o esadecimale? e utilizzando le macro definite in `sys/stat.h <https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_stat.h.html>`_?

Riferimenti
"""""""""""

* :posix:`stdin <stdin>`
* :posix:`close <close>`
* :posix:`open <open>`
* :posix:`exec <exec>`
* `mode_t <https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_stat.h.html>`_
* `Microsoft C docs on literals <https://docs.microsoft.com/cpp/c-language/c-integer-constants>`_






