19/10/2022 - Processi parte 1 - Thread parte 1 
-----------------------------------------------

* Processi
  
  * Processi UNIX: stati, gerarchie e threads
  * Processi Linux: concetto di task, stati, accenni di task_struct

* Thread
  
  * Concetto di thread
  * User-Level threads e Kernel-level threads
  * POSIX threads
  * Variabili per thread
  * Librerie thread-safe e non
  * pthread_create, pthread_join, pthread_exit

Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <books2022>`] Sezione 3.6, 4.1, 4.2
* [:ref:`t2 <books2022>`] Sezione 3.2, 4.1, 4.2, 4.3, 4.4, 4.4.1, 4.6.4, 4.7.2

Link di approfondimento
"""""""""""""""""""""""

* `pthread_create <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_create.html>`_
* `pthread_join <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_join.html>`_
* `pthread_exit <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_exit.html>`_
* Codice sorgente Linux Kernel: `task_struct <https://elixir.bootlin.com/linux/v5.14.7/source/include/linux/sched.h#L661>`_
* `pthread_key_create <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_key_create.html>`_
* `pthread_key_delete <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_key_delete.html>`_
* `pthread_getspecific <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getspecific.html>`_
* `GCC Thread Local Storage <https://gcc.gnu.org/onlinedocs/gcc/Thread-Local.html>`_
    





18/10/2022 - Processi parte 3
------------------------------------------------------------------------

* Processi:

    * Famiglia di funzioni POSIX exec
    * Ambiente e variabili di ambiente
    * Famiglia di funzioni POSIX getenv, putenv, setenv, unsetenv
    * Shell Linux: ls, man, cd

Riferimenti libro di testo
""""""""""""""""""""""""""



* [:ref:`t1 <books2022>`] Sezione 2.3
* [:ref:`t2 <books2022>`] Sezione 3.1.2, 3.3.1
* [:ref:`t3 <books2022>`] Sezione 3.2, 3.3

Link di approfondimento
"""""""""""""""""""""""

* `exec <https://pubs.opengroup.org/onlinepubs/9699919799/functions/exec.html>`_
* `getenv <https://pubs.opengroup.org/onlinepubs/9699919799/functions/getenv.html>`_
        