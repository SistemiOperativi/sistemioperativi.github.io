.. toctree::
   :hidden:
   
   linux_install
   examples
   slides
   lectures/index
   

Sistemi Operativi
=============================================

Benvenuti al corso di Sistemi Operativi per A.A. 2021/2022 del Corso di Laurea in Ingegneria Informatica di Roma Tre

Docente: `Romolo Marotta <https://romolomarotta.github.io>`_


Obiettivi del corso
===================

L'obiettivo del corso è fornire allo studente competenze sull'architettura di un generico sistema operativo moderno, con particolare riferimento al sistema Linux, 
e sulle metodologie usate per risolvere le problematiche tipiche della gestione di risorse in un sistema operativo moderno.
Infine, particolare attenzione verrà dedicata alla programmazione di sistema e scripting.


Orario delle lezioni
--------------------

=========  =============  =====
Giorno     Orario         Aula 
=========  =============  =====
Martedì    16:00 - 18:00  N13 [Vasca Navale 79/81] - `Aula Teams <https://teams.microsoft.com/l/meetup-join/19%3aRhhdoEO6QOI_oVGAqU-Q6ba9bxYJongS7KxMWkRTe981%40thread.tacv2/1633386278580?context=%7b%22Tid%22%3a%22ffb4df68-f464-458c-a546-00fb3af66f6a%22%2c%22Oid%22%3a%22430d18c0-6f97-4e80-834a-955f8618ef03%22%7d>`_ 
Mercoledì  16:00 - 18:00  N13 [Vasca Navale 79/81] - `Aula Teams <https://teams.microsoft.com/l/meetup-join/19%3aRhhdoEO6QOI_oVGAqU-Q6ba9bxYJongS7KxMWkRTe981%40thread.tacv2/1633386278580?context=%7b%22Tid%22%3a%22ffb4df68-f464-458c-a546-00fb3af66f6a%22%2c%22Oid%22%3a%22430d18c0-6f97-4e80-834a-955f8618ef03%22%7d>`_ 
=========  =============  =====


Link ai contenuti del corso
---------------------------

- `Teams <https://teams.microsoft.com/l/team/19%3aRhhdoEO6QOI_oVGAqU-Q6ba9bxYJongS7KxMWkRTe981%40thread.tacv2/conversations?groupId=098a73ce-8602-46e3-84c6-8107ebe1a9ae&tenantId=ffb4df68-f464-458c-a546-00fb3af66f6a>`_
- `SharePoint <https://uniroma3.sharepoint.com/sites/AA2122-SISTEMIOPERATIVI-20801961MAROTTA>`_
- `Stream  <https://web.microsoftstream.com/group/098a73ce-8602-46e3-84c6-8107ebe1a9ae>`_
- `GitHub  <https://github.com/SistemiOperativi>`_
- :doc:`Slides <slides>`

Ricevimento
-----------

Contattare il docente alla seguente email **{nome}.{cognome}@uniroma3.it** e riportare il prefisso **[SO2122]** nell'oggetto.


Modalità d'esame
----------------

L'esame prevede una prova con:

* Domande di teoria (65% del voto)
* Esercizi di programmazione (35% del voto)


.. _books:

Testi consigliati e link utili (in aggiornamento)
-------------------------------------------------

* [t1] Operating Systems: Internals and Design Principles - William Stallings - Prentice Hall, fifth edition (o superiori). Riferimento: ninth global edition.
* [t2] Sistemi operativi: Concetti ed Esempi - Silberschatz Abraham, Galvin Peter Baer, Gagne Greg - Addison Wesley/Pearson, nona edizione (o superiori). Riferimento: tenth global edition.
* [t3] Programmazione in Ambiente UNIX - Francesco Quaglia, Camil Demetrescu - `Disponibile in formato pdf <https://francescoquaglia.github.io/TEACHING/SISTEMI-OPERATIVI/AA-2020-2021/TEXTS/dispensa.pdf>`_




Programma
---------

* **Panoramica sui sistemi operativi moderni.** definizione di sistema operativo, scopi, architettura a strati, kernel/user mode, caratteristiche salienti
* **Processi e Thread.** dispatching, stati, descrizione e controllo, modelli tipici di sistemi operativi e di uso della memoria nei processi
* **Memoria.** allocatori di memoria, partitioning, best/first/next fit, buddy algorithm, paging, segmentation, memoria virtuale e sua gestione hardware/software 
* **Scheduling.** a breve medio e lungo termine, algoritmi per cpu scheduling
* **I/O e File Management.** Disk scheduling, RAID, UNIX File Management, inode, Linux VFS, ext2
* **Sincronizzazione.** primitive di sincronizzazione, RMW, mutex, semafori
* **Introduzione a Linux.** comandi di utilizzo frequente (e.g., gestione file e directory), variabili di ambiente, piping, redirection, segnali, espressioni regolari (sed e grep), scripting (bash, awk), linux filesystem management
* **Debugger.** utilizzo di gdb stepping, breakpoints, watching, backtrace, comandi gdb.
* **Programmazione di Sistema.** Gestione in C dei processi/thread su ambiente linux
* **Virtualizzazione.** Concetti generali, container, Docker

