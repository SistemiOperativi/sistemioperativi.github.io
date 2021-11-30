.. role:: raw-html(raw)
   :format: html

Flip vector
===========


:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/flip_vector/flip_vector.c">FlipVector</a>
<a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/flip_vector/flip_vector.c"></a>`
è un programma C il cui obiettivo è mostrare diversi aspetti nell'utilizzo e gestione dei thread.

In questo programma vengono creati molteplici thread che manipolano un array condiviso.
Nello specifico, ciascun thread inverte ripetutamente la posizione di ciascuna entry nell'array, la cui dimensione è un numero pari.
A seguire, la funzione stress test implemente tale operazione:


.. code-block:: c
    
    void* stress_test(void *arg){
        long my_ops = 0;
        int i = 0;
        pthread_barrier_wait(&ptbarrier);

        while(!stop){
            acquire();
            for(i=0;i<ARRAY_LEN/2;i++){
                shared[i] ^= shared[ARRAY_LEN-1-i]; 
                shared[ARRAY_LEN-1-i] ^= shared[i];  
                shared[i] ^= shared[ARRAY_LEN-1-i]; 
            }
            release();
            my_ops+=1;
        }
        
        __sync_fetch_and_add(&ops, my_ops);
        return NULL;
    }

.. question_note::
    Come modificare la condizione di terminazione del ciclo interno per gestire array di taglia generica?

.. observation_note::
    L'operatore :code:`^` implementa la semantica di eXclusive OR (`XOR <https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html#Bitwise-Logical-Operators>`_) bit a bit. La relativa tabella di verità è la seguente:

    ===  ===  =====
     X    Y    X^Y
    ===  ===  =====
     0    0     0
     0    1     1
     1    0     1 
     1    1     0
    ===  ===  =====   

    In altre parole se i due bit di input sono uguali l'output è pari a 0. Viceversa se sono diversi l'output è pari ad 1. Di conseguenza, 
    :code:`x^x=0`.

    .. question_note::
        Come è stata utilizzato lo XOR per implementare lo scambio del contenuto di due variabili?

Chiaramente, essendo l'array condiviso, è necessaria della sincronizzazione al fine di manipolare correttamente l'array.
Le funzioni :code:`acquire` e :code:`release` assolvono a questo scopo, utilizzando nella loro implementazione primitive di lock.  
Il programma inoltre misura le perfomance dell'applicazione in termini di sezioni critiche eseguite.
Per assicurarsi che ciascun thread lavori con la massima concorrenza, questi aspettano che tutti i thread raggiungono la medesima riga di codice,
prima di cominciare a manipolare l'array.
Questo è ottenuto grazie alla primitiva di sincronizzazione :code:`pthread_barrier_wait`, che blocca un thread fintanto che N thread non ne invocano la medesima funzione sul medesimo oggetto opportunamente inizializzato a N. 

.. observation_note::
  
  Una barriera può esser vista come un semaforo che:

  * può assumere valori negativi
  * inizializzato a -N
  * l'operazione di wait incrementa il contatore di 1 unità
     * se il semaforo è negativo il thread rimane bloccato in attesa
     * se il semaforo assume valore pari a 0, tutti i thread in attesa vengono sbloccati e il valore resettato a -N

Prima di terminare ciascun thread utilizza una RMW per incrementare un contatore globale :code:`ops` del numero di operazioni complessivamente eseguite dai thread. 
A tal scopo si è utilizzata la funzione :code:`__sync_fetch_and_add`.

.. warning::
   Le operazioni builtin __sync di gcc sono semplici da utilizzare, ma deprecate. 
   La versione di riferimento sono le `__atomic builtin <https://gcc.gnu.org/onlinedocs/gcc/_005f_005fatomic-Builtins.html#g_t_005f_005fatomic-Builtins>`_, che tuttavia tengono conto anche del modello di memoria secondo lo 
   `standard C++11 <https://en.cppreference.com/w/cpp/atomic/memory_order>`_. 
   Per ulteriori dettagli consultare `AtomicSync <https://gcc.gnu.org/wiki/Atomic/GCCMM/AtomicSync>`_.

.. question_note::
    Come è possibile implementare l'accumulo del numero di operazioni globalmente eseguite senza utilizzare istruzioni RMW?

Ciascun thread termina non appena la variabile :code:`stop` assume valore pari a :code:`true`.

Il test viene ripetuto con molteplici configurazioni, ossia al variare dei thread **e** del tipo di lock.
Il tutto è coordinato dal main thread secondo lo schema che segue. 

.. code-block:: c

    for(i=1;i<=MAX_THREADS;i<<=1)
    {
        for(lock_type=0; lock_type<num_locks;lock_type++){
            ...
            ...
            pthread_barrier_init(&ptbarrier, NULL, i);

            for(j=0;j<i;j++)    pthread_create(ptids +j, NULL, stress_test, NULL);
            sleep(SECONDS);
            __sync_bool_compare_and_swap(&stop, 0, 1);
            
            for(j=0;j<i;j++)    pthread_join(ptids[j],  NULL);

            pthread_barrier_destroy(&ptbarrier);
        }
    }

.. observation_note:: 
    L'operatore :code:`<<` è l'operatore di `shift <https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html#Bit-Shifting>`_ a sinistra.
    Considerando una variabile *x* a 8 bit con valore 4 la sua rappresentazione è 0000 0100.
    L'istruzione :code:`x << 1` indica l'operazione di shift a sinistra di una posizione della variabile *x*, il cui risultato è pari a 
    0000 1000, ossia x assume il valore 8.
    L'operatore :code:`>>` è l'operatore di shift a destra.

.. question_note::
   
   * Quali operazioni matematiche possono essere implementate tramite gli operatori :code:`<<` e :code:`>>`?
   * Quante iterazioni esegue il seguente ciclo :code:`for(i=1;i<=MAX_THREADS;i<<=1)`?


Per ciascun test, il main thread:

  * inizializza la barriera
  * crea i thread
  * va in sleep per :code:`SECONDS` secondi
  * setta la variabile :code:`stop` ad 1 con un'istruzione atomica
  * attende la terminazione di ciascun thread
  * distrugge la barriera

La variabile :code:`lock_type` è una variabile globale utilizzata all'interno di :code:`acquire` e :code:`release` per selezionare l'implementazione di lock da utilizzare.

.. question_note::
    * Perché la barriera viene distrutta ad ogni fine iterazione e inizializzata ad inizio iterazione?
    * Quale altra istruzione RMW poteva essere usata al posto della compare&swap?


L'impostazione del test è tale per cui si misurano il numero di operazioni effettuate in concorrenza da tutti i thread in un intervallo di tempo predefinito.
Inoltre, prima di eseguire il suddetto ciclo, il main thread:

  * inizializza le primitive di lock della libreria pthread

    .. code-block:: c

        pthread_spin_init(&ptspin,  PTHREAD_PROCESS_PRIVATE);
        pthread_mutex_init(&ptmutex, NULL);

  * limita i core su cui i thread possono andare in esecuzione

    .. code-block:: c

        cpu_set_t my_set;      
        CPU_ZERO(&my_set); 
        for(i=0;i<CORES;i++)
            CPU_SET(i, &my_set);
        sched_setaffinity(0, sizeof(cpu_set_t), &my_set);
  
.. warning::
    sched_affinity è una funzione non POSIX

.. question_note::
    * Perché la set affinity viene utilizzata dal main thread? 
    * L'uso di set affinity garantisce che ciascun thread andrà in esecuzione sul medesimo core? Se sì, perché? Se no, come è possibile garantirlo? 

Le funzioni di acquire e release
""""""""""""""""""""""""""""""""

Le funzione di acquire e release utilizzano una specifica implementazione di lock in funzione del valore assunto dalla variabile globale :code:`lock_type`.
Nello specifico supportano 5 implementazioni differenti di lock:

#. pthread spin lock (PT_TAS)
#. pthread mutex (PT_MUTEX)
#. test-and-set spin lock (TAS)
#. test-and-test-and-set spin lock (TTAS)
#. ticket spin lock (TICKET)

Nel caso di lock forniti dalla libreria pthread, acquire e release ridirezionano sulle rispettive funzioni di libreria.

.. code-block:: c

    void acquire(){
        ...
        if(lock_type == PT_TTAS) pthread_spin_lock(&ptspin);
        if(lock_type == PT_MUTEX)pthread_mutex_lock(&ptmutex);
    }

    void release(){
        ...
        if(lock_type == PT_TTAS)                    pthread_spin_unlock(&ptspin);
        if(lock_type == PT_MUTEX)                   pthread_mutex_unlock(&ptmutex);
    }

Chiaramente le variabili *ptspin* e *ptmutex* sono variabili globali.

Anche i lock TAS e TTAS sono delle variabili globali intere.
Il valore 0 indica che il lock è libero e 1 indica che il lock è stato acquisito da un qualche thread.

.. code-block:: c

    volatile int lock = 0;

    void acquire(){
        if(lock_type == TAS)
            while(__sync_lock_test_and_set(&lock,1));
        if(lock_type == TTAS){
            while(__sync_lock_test_and_set(&lock,1))
                while(lock);
        }
        ...
    }

    void release(){
        if(lock_type == TAS || lock_type == TTAS){  asm volatile ("":::"memory");   lock = 0;}
        ...
    } 

.. observation_note::  
    
    * la varibile *lock* è dichiarata **volatile**. Questo garantisce che il compilatore non attuerà alcune ottimizzazioni, garantendo che ogni accesso alla variabile *lock* verrà effettuato sempre in memoria. Ad esempio, il compilatore non potrà usare i registri general purpose come cache per la variabile.
    * :code:`asm volatile ("":::"memory");` costituisce una barriera per il compilatore. Di conseguenza, quest'ultimo non può spostare istruzioni che seguono la barriera prima di quest'ultima e viceversa. *asm* indica al compilatore che si sta innestando all'interno di codice C del codice assembly. 
      In questo caso, l'istruzione innestata :code:`""` è nulla.
      Siccome, il codice innestato è nullo, è necessario indicare al compilatore di non eliminare l'istruzione tramite il token **volatile**.
      Infine, l'ultimo parametro :code:`"memory"` indica al compilatore che l'istruzione accede in modo impredicibile alla memoria, disabilitando ulteriori ottimizzazioni come il riordinamento delle operazioni di scrittura/lettura.
      Per approfondimenti sul tema consultare la documentazione di GCC riguardo gli `extended-asm <https://gcc.gnu.org/onlinedocs/gcc-4.7.2/gcc/Extended-Asm.html>`_.

.. note::
    Provare a dichiarare la variabile *lock* come **int** piuttosto che **volatile int** e vederne gli effetti quando si compila con il massimo livello di ottimizzazione (e.g. :code:`gcc -O3`). 

Infine, il ticket lock (TICKET) è implementato come una coppia di variabili globali *lock* e *now* di tipo **volatile int**, che indicano rispettivamente l'ultimo ticket servito e il ticket corrente. 

.. code-block:: c

    volatile int lock = 0;
    ...
    volatile int now = 0;

    void acquire(){
        ...
        if(lock_type == TICKET){
            int myticket = __sync_fetch_and_add(&lock, 1);
            while(now != myticket);
        }
        ...
    }

    void release(){
        ...
        if(lock_type == TICKET){                    asm volatile ("":::"memory");   now = now+1;}
        ...
    }

.. question_note::
    L'algoritmo di ticket lock mostrato è corretto? Se sì, cercare di mostrare perché? Se no, mostrare un caso in cui l'algoritmo non garantisce mutua eclusione o progresso.

Riferimenti
"""""""""""

* :posix:`pthread_barrier_init <pthread_barrier_init>`
* :posix:`pthread_barrier_wait <pthread_barrier_wait>`
* `bitwise XOR <https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html#Bitwise-Logical-Operators>`_
* `__sync gcc builtin <https://gcc.gnu.org/onlinedocs/gcc/_005f_005fsync-Builtins.html>`_
* :posix:`pthread_spin_init <pthread_spin_init>`
* :posix:`pthread_mutex_init <pthread_mutex_init>`
* :linux2:`sched_setaffinity <sched_setaffinity>`
* :linux3:`CPU_SET <CPU_SET>`
* `shift <https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html#Bit-Shifting>`_
* `extended-asm <https://gcc.gnu.org/onlinedocs/gcc-4.7.2/gcc/Extended-Asm.html>`_






