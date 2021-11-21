Diario delle lezioni
=====================


17/11/2021 - Gestione della memoria parte 2
-------------------------------------------

* Segmentazione
* Segmentazione paginata
* Mappatura dello spazio di indirizzamento e relativi system call Linux
* Introduzione alla memoria virtuale

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 7.4, 8.1
* [:ref:`t2 <books>`] Sezione 9.6, 10.1


Link di approfondimento
"""""""""""""""""""""""

* `POSIX mmap <https://pubs.opengroup.org/onlinepubs/9699919799/functions/mmap.html>`_
* `Linux mmap <https://man7.org/linux/man-pages/man2/mmap.2.html>`_

-----------------------------------------------------------------------------------


16/11/2021 - Gestione della memoria parte 2
-------------------------------------------

* Binding di indirizzi
* Concetto di rilocazione
* Paginazione
* Tabella delle pagine, Traslation Lookaside Buffer, Paginazione gerarchica

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 7.3, 8.1 paragrafo Paging
* [:ref:`t2 <books>`] Sezione 9.1.1, 9.1.2, 9.1.3, 9.3, 9.3.1, 9.3.2, 9.3.3, 9.3.2, 9.4, 9.4.1

-----------------------------------------------------------------------------------
















10/11/2021 - Sincronizzazione parte 4 - Gestione della memoria parte 1
----------------------------------------------------------------------

* Semafori POSIX
* Introduzione a gestione della memoria
* Partizioni fisse
* Partizioni dinamiche
* Politiche di placement: Best fit, Worst fit, First fit, Next fit
* Buddy system
* Frammentazione interna ed esterna

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 7.1, 7.2
* [:ref:`t2 <books>`] Sezione 6.6, 7.3.2, 9.1, 9.1.1, 9.2, 9.2.1, 9.2.3 

Link di approfondimento
"""""""""""""""""""""""

* `sem_init <https://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_init.html>`_
* `sem_wait <https://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_wait.html>`_
* `sem_post <https://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_post.html>`_
* `sem_destroy <https://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_destroy.html>`_

-----------------------------------------------------------------------------------

09/11/2021 - Sincronizzazione parte 3
-------------------------------------

* Read-Modify-Write
* Algoritmi di mutua esclusione basati su RMW
* Spin lock, Mutex POSIX

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 5.3
* [:ref:`t2 <books>`] Sezione 6.4, 6.5, 6.6, 7.3.1

Link di approfondimento
"""""""""""""""""""""""

* `pthread_spin_init <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_init.html>`_
* `pthread_spin_lock <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_lock.html>`_
* `pthread_mutex_init <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_init.html>`_
* `pthread_mutex_lock <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_lock.html>`_
* `gcc sync builtins <https://gcc.gnu.org/onlinedocs/gcc/_005f_005fsync-Builtins.html#g_t_005f_005fsync-Builtins>`_





-----------------------------------------------------------------------------------











03/11/2021 - Sincronizzazione parte 2
-------------------------------------

* Mutua Esclusione
* Errori Comuni: Deadlock e Livelock
* Algoritmo di Peterson
* Algoritmo del panettiere (Lamport)

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 5.1, 5.2, 6.1
* [:ref:`t2 <books>`] Sezione 6.3, 6.8, 8.2, 8.3

Link di approfondimento
"""""""""""""""""""""""

* `Backery algorithm <http://lamport.azurewebsites.net/pubs/bakery.pdf>`_

-----------------------------------------------------------------------------------

02/11/2021 - CPU scheduling parte 4 - Sincronizzazione parte 1
--------------------------------------------------------------

* Scheduler UNIX System V Release 4
* Linux Complete Fair Scheduler
* Introduzione alla sincronizzazione

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 10.3, 10.4, 5
* [:ref:`t2 <books>`] Sezione 5.7.1, 6.1, 6.2

Link di approfondimento
"""""""""""""""""""""""

* `Complete Fair Scheduler <https://www.kernel.org/doc/html/latest/scheduler/sched-design-CFS.html>`_

















-----------------------------------------------------------------------------------




27/10/2021 - CPU scheduling parte 3
-----------------------------------

* Multi-level feedback queue
* Fair-share scheduling
* Multiprocessor scheduling
* Load sharing
* Load balancing
* Affinity

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 9.2, 10.1
* [:ref:`t2 <books>`] Sezione 5.5

Link di approfondimento
"""""""""""""""""""""""

* `sched_setaffinity <https://man7.org/linux/man-pages/man2/sched_setaffinity.2.html>`_
* `sched_getaffinity <https://man7.org/linux/man-pages/man2/sched_getaffinity.2.html>`_
* `CPU_SET <https://man7.org/linux/man-pages/man3/CPU_SET.3.html>`_
* `pthread_setaffinity_np <https://man7.org/linux/man-pages/man3/pthread_setaffinity_np.3.html>`_

-----------------------------------------------------------------------------------


26/10/2021 - CPU scheduling parte 2
-----------------------------------

* First Come First Serve
* Shortest Job First
* Round Robin
* Priority Scheduling

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 9.2
* [:ref:`t2 <books>`] Sezione 5.3










-----------------------------------------------------------------------------------








20/10/2021 - Threads parte 2 - CPU scheduling parte 1
-----------------------------------------------------

* pthread_create, pthread_join, pthread_exit
* Processi UNIX: stati, gerarchie e threads
* Processi Linux: concetto di task, stati, accenni di task_struct
* Introduzione al CPU scheduling: metriche di prestazionali e non per l'utente ed il sistema, preemtive e non-preemptive scheduling

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 3.6, 9.1, 9.2
* [:ref:`t2 <books>`] Sezione 3.2, 4.6.4, 4.7.2, 5.1, 5.2

Link di approfondimento
"""""""""""""""""""""""

* `pthread_create <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_create.html>`_
* `pthread_join <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_join.html>`_
* `pthread_exit <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_exit.html>`_
* Codice sorgente Linux Kernel: `task_struct <https://elixir.bootlin.com/linux/v5.14.7/source/include/linux/sched.h#L661>`_
        
-----------------------------------------------------------------------------------


19/10/2021 - Processi parte 5 - Threads parte 1
-----------------------------------------------

* Concetto di thread
* User-Level threads e Kernel-level threads
* POSIX threads
* Variabili per thread
* Librerie thread-safe e non

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 4.1, 4.2
* [:ref:`t2 <books>`] Sezione 4.1, 4.2, 4.3, 4.4, 4.4.1, 4.6.4

Link di approfondimento
"""""""""""""""""""""""

* `pthread_key_create <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_key_create.html>`_
* `pthread_key_delete <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_key_delete.html>`_
* `pthread_getspecific <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getspecific.html>`_
* `GCC Thread Local Storage <https://gcc.gnu.org/onlinedocs/gcc/Thread-Local.html>`_
    



-----------------------------------------------------------------------------------















13/10/2021 - Processi parte 4
-----------------------------

* Posix fork
* Layout di programma C
* Famiglia di funzioni POSIX exec
* Ambiente e variabili di ambiente
* Famiglia di funzioni POSIX getenv, putenv, setenv, unsetenv
* Utilizzo documentazione online e da riga di comando Linux (man)
* Shell Linux: ls, man, fg, bg, top e token !

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 2.3
* [:ref:`t2 <books>`] Sezione 3.1.2, 3.3.1
* [:ref:`t3 <books>`] Sezione 3.2, 3.3

Link di approfondimento
"""""""""""""""""""""""

* `exec <https://pubs.opengroup.org/onlinepubs/9699919799/functions/exec.html>`_
* `getenv <https://pubs.opengroup.org/onlinepubs/9699919799/functions/getenv.html>`_
        
-----------------------------------------------------------------------------------

12/10/2021 - Processi parte 3
-----------------------------

* Process switch
* Cambio di modo e cambio di contesto
* Servizi di sistema per la gestione di processi
* POSIX fork, exit, wait
* Gerarchie di processi
* Utilizzo documentazione online e da riga di comando Linux (man)
* Shell Linux: ls, man, fg, bg e token !

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 3.4, 
* [:ref:`t2 <books>`] Sezione 3.2.3, 3.3.1, 3.3.2
* [:ref:`t3 <books>`] Sezione 1.2, 3.1

Link di approfondimento
"""""""""""""""""""""""

* `fork <https://pubs.opengroup.org/onlinepubs/9699919799/functions/fork.html>`_
* `exit <https://pubs.opengroup.org/onlinepubs/9699919799/functions/exit.html>`_
* `wait <https://pubs.opengroup.org/onlinepubs/9699919799/functions/wait.html>`_

-----------------------------------------------------------------------------------


















06/10/2021 - Processi parte 2
-----------------------------

* Stato di un processo e code: 5 stati
* Strutture di controllo di un Sistema Operativo
* Long, mid, short term scheduling
* Process switch

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 3.2, 3.3, 9.2
* [:ref:`t2 <books>`] Sezione 2.3.1, 2.3.2, 2.8, 3.1.2, 3.2

-----------------------------------------------------------------------------------


05/10/2021 - Introduzione parte 3 - Processi parte 1
----------------------------------------------------

* Introduzione:

    * System call
    * Librerie Standard
    * Architettura dei Sistemi Operativi

* Processi:

    * Immagine
    * Process Control Block
    * Stato di un processo: 2 stati, 3 stati
    * Code di processi

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 2.7, 2.8, 3.1, 3.2
* [:ref:`t2 <books>`] Sezione 2.3.1, 2.3.2, 2.8, 3.1.1, 3.1.3 

-----------------------------------------------------------------------------------



















29/09/2021 - Introduzione parte 2
---------------------------------

* Sistemi operativi: elementi chiave
* Interrupt: eventi, supporto hardware
* Interrupt-driven os: protezione delle risorse (istruzioni privilegiate, protezione memoria, timer) e accesso a codice di sistema operativo (system call)

Riferimenti libro di testo
""""""""""""""""""""""""""
* [:ref:`t1 <books>`] Sezione 1.1, 1.2, 1.3, 1.4
* [:ref:`t2 <books>`] Sezione 1.2, 2.3.1, 2.3.2 

Link di approfondimento
"""""""""""""""""""""""

* Codice sorgente Linux Kernel: `IDT <https://elixir.bootlin.com/linux/v5.14.7/source/arch/x86/kernel/idt.c#L79>`_

-----------------------------------------------------------------------------------


28/09/2021 - Introduzione parte 1
---------------------------------

* Sistemi operativi: definizione ed obiettivi
* Evoluzione dei sistemi operativi: Sistemi seriali, Sistemi batch, Sistemi time-sharing, Sistemi Real time, Multicore, Dark silicon
* Sincronizzazione e Speedup: concetto di lock e legge di Amdahl

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books>`] Sezione 2.1, 2.2, 2.3, 4.3
* [:ref:`t2 <books>`] Sezione 1.1, 1.4, 2.7


Link di approfondimento
"""""""""""""""""""""""

* `The free lunch is over <http://www.gotw.ca/publications/concurrency-ddj.htm>`_
* `Legge di Amdahl Sezione 4 Eq. 11 <https://dl.acm.org/doi/pdf/10.5555/110382.110450>`_
                        











