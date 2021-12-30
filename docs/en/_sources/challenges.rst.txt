Sfide
=====

Requisiti
-----------

Per sottomettere la propria soluzione ad una sfida è necessario aver compiuto i seguenti passi preliminari:

#. Avere un account GitHub 
#. Accedere al link all'assignment di benvenuto: `<https://classroom.github.com/a/qU7ZFhmv>`_
#. Associare l'account GitHub al codice identificativo ricevuto via email

 #. Cerca il tuo identificativo utilizzando la funzione ricerca del tuo browser (crtl+f testato su firefox e google chrome)
 #. Clicca sul tuo identificativo
 #.	Controlla di aver selezionato l'identificativo corretto
 #. Premi ok

4.	Accetta l'assignment *GitFundamentals*



Sfida 1: La password del docente
-----------------------------------------

Stato:**OPEN**

Nel corso della lezione :ref:`l22-12-2021` sono state trattate alcune tematiche relative ad aspetti di sicurezza.
In particolare, si è discusso il ruolo dei file */etc/passwd* e */etc/shadow* in sistemi GNU/Linux.
Inoltre, sono stati illustrati alcuni dettagli riguardo i permessi ed il contenuto del file *shadow*.
Nello specifico, è stato descritto come individuare:
 
 * l'hash della password di un utente;
 * il sale relativo;
 * l'algoritmo di hash utilizzato.

Dopo 81 minuti e 30 secondi di lezione, il docente ha mostrato il file *shadow* installato su un suo dispositivo e l'entry relativa alla sua utenza.

La sfida
""""""""

Individuare la password del docente.

I premi
"""""""

* 1 punto sul voto finale per la prima soluzione che individua la password corretta

Le regole
"""""""""

Per sottomettere la soluzione è necessario:

#. accetta l'assignment su GitHub: `<https://classroom.github.com/a/oRfof8ZI>`_
#. pubblica sul repository il codice utilizzato per individuare la password e un Readme 
#. inviare una email con oggetto [OS2122-CHALLENGE-1] con:

  #. l'hash del commit con il codice da sottomettere a valutazione 
  #. la matricola

Una soluzione è ritenuta valida se:

#. è stata inviata correttamente
#. NON utilizza programmi per il crack/recovery delle password (e.g. Hashcat, John the Ripper). Tuttavia, è ammesso l'utilizzo dei seguenti strumenti per lo sviluppo di soluzioni ad hoc:

  * `openssl <https://linux.die.net/man/1/openssl>`_
  * `GNU crypt <https://ftp.gnu.org/old-gnu/Manuals/glibc-2.2.3/html_node/libc_650.html>`_ 
  * `crypt <https://man7.org/linux/man-pages/man3/crypt.3.html>`_

Infine, non è possibile sottomettere più di una soluzione.
In caso di sottomissione multipla, verrà considerata la prima in ordine cronologico.

Scadenze
""""""""

* La sfida rimane aperta fintanto che i punti non sono stati assegnati.
* I punti possono essere acquisiti entro e non oltre l'A.A. 2021/2022.