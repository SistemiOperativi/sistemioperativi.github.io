.. role:: raw-html(raw)
   :format: html

CoPy
==========


:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/cp/cp.c">CoPy</a>
<a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/cp/cp.c"></a>`
è un programma C il cui obiettivo è mostrare l'utilizzo di alcuni servizi per la gestione di file.

.. code-block:: c
    :linenos:
    
    #include <stdio.h>
    #include <fcntl.h>
    #include <stdlib.h>
    #include <unistd.h>

    #define BUFSIZE 250

    #define abort(msg) do{printf(msg);exit(1);}while(0)

    int main(int argc, char *argv[]) {
        int ifd, ofd, size_r, size_w, end = 0; 
        char buffer[BUFSIZE];

        /* check parameters */
        if (argc != 3) abort("usage: copy <source> <target>\n");

        /* open the input file and check errors */
        ifd=open(argv[1],O_RDONLY);
        if (ifd == -1) abort("input open error\n");
        
        /* opend output file and check errors */
        ofd=open(argv[2],O_WRONLY|O_CREAT|O_TRUNC,0660); 
        if (ofd == -1) abort("output creation error\n");
        
        while(!end){
            /* read up to BUFSIZE from input file and check errors */
            size_r=read(ifd,buffer,BUFSIZE);
            if (size_r == -1) abort("read error\n"); 

            /* has EOF been reached? */
            end = size_r == 0;

            /* write BUFSIZE to destination file */ 
            size_w = write(ofd,buffer,size_r);             
            if (size_w == -1) abort("write error\n");
            printf("written: %d\n", size_w);
        } 

        /* close file descriptors */
        close(ifd);
        close(ofd);
    }

Il programma prende da riga di comando il file da copiare ed il file destinazione.
Lo schema è il seguente:

#. apre il file di input in lettura utilizzando il flag O_RDONLY (riga 18)
#. crea ed apre il file di output in sola scrittura tramite i flag O_CREAT e O_WRONLY, e, se già esistente, ne cancella il contenuto grazie al flag O_TRUNC (riga 22)
#. legge al più BUFSIZE byte su un buffer (riga 27)
#. utilizza il suddetto buffer per la scrittura su file di output (riga 34)
#. una volta letto e copiato tutto il file (riga 45) vengono chiusi i relativi file descriptor (riga 40 e 41)

.. warning:
  
  Il codice mostrato è affetto da una problematica relativa alla fase di scrittura.
  Nello specifico, è possibile che il programma termini correttamente senza però aver effettuato una correta copia del file.

.. question_note:
    
  * In quali scenari il programma presenta la suddetta anomalia? 
  * Come prevenirla? 





Riferimenti
"""""""""""

* :posix:`open <open>`
* :posix:`read <read>`
* :posix:`write <write>`
* :posix:`close <close>`






