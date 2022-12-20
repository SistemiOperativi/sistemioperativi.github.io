09/11/2021 - CPU scheduling parte 2
-------------------------------------


* Round Robin
* Priority Scheduling
* Multi-level feedback queue
* Fair-share scheduling
* Multiprocessor scheduling
* Load sharing
* Load balancing
* Affinity

-----------------------------------------------------------------------------------

Riferimenti libro di testo
""""""""""""""""""""""""""
* [:ref:`t1 <textbooks>`] Sezione 9.2, 10.1
* [:ref:`t2 <textbooks>`] Sezione 5.4, 5.5


08/11/2021 - Sincronizzazione parte 4 - CPU scheduling parte 1
----------------------------------------------------------------------

* Sincronizzaione
 
  * Spin lock, Mutex POSIX
  * Semafori POSIX

* CPU scheduling

  * Metriche per cpu scheduling
  * Non-preemptive vs Preemtive
  * First Come First Serve
  * Shortest Job First


Riferimenti libro di testo
""""""""""""""""""""""""""

* [:ref:`t1 <textbooks>`] Sezione 9.1, 9.2
* [:ref:`t2 <textbooks>`] Sezione 6.6, 7.3.1, 5.1, 5.2, 5.3

Link di approfondimento
"""""""""""""""""""""""

* `pthread_spin_init <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_init.html>`_
* `pthread_spin_lock <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_lock.html>`_
* `pthread_mutex_init <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_init.html>`_
* `pthread_mutex_lock <https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_lock.html>`_
* `gcc sync builtins <https://gcc.gnu.org/onlinedocs/gcc/_005f_005fsync-Builtins.html#g_t_005f_005fsync-Builtins>`_
* `sem_init <https://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_init.html>`_
* `sem_wait <https://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_wait.html>`_
* `sem_post <https://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_post.html>`_
* `sem_destroy <https://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_destroy.html>`_
