:orphan:

8- Programmazione
""""""""""""""""""

.. comment:
  #. Nei sistemi operativi UNIX, `/dev/urandom <https://man7.org/linux/man-pages/man4/random.4.html>`_ è un dispositivo a caratteri (char device) virtuale in grado di generare numeri casuali. 
     Nello specifico, l'operazione di lettura dal relativo file produce byte casuali. 
     Scrivere un programma C che genera un file con contenuto interamente randomico. Il programma:

      * prende come parametri da linea di comando: un numero *N* e una stringa *S* da usare come nome del file da creare;
      * crea un file *S* contenente *N* byte randomici;
      * utilizza il dispositivo /dev/random come sorgente di numeri pseudo-casuali. 

  #. Dato un file binario contenente un sequenza di 2^15 interi di tipo *short*, scrivere un programma che crea N processi o threads, i quali leggono il contenuto del file ed individuano il valore minimo e massimo contenuto nel file. Nel fornire una soluzione rispettare i seguenti vincoli:
    
    * ciascun intero non può essere letto da più di un thread/processo;
    * ciascun thread/processo può leggere il medesimo intero al più una volta;
    * ciascun thread/processo può allocare memoria nell'heap per al più 512 byte;
    * N è un parametro definito a tempo di compilazione o tramite linea di comando;
    * N è minore o uguale a 8;
    * è ammesso allocare di variabili globali (data) e locali (stack) per memorizzare tipi primitivi (puntatori, int, short, char, long, etc.) per al più 128 byte.
    
    Per generare il file è possibile utilizzare la soluzione dell'esercizio 1.

  3. Scrivere un programma C *invert* che dato un file *A* ne inverte il contenuto e lo memorizza in nuovo file *B*. Il programma deve:
    
    * riportare il contenuto di *A* in memoria;
    * invertire la posizione di ciascun byte utilizzando un numero *N* di thread/processi concorrenti;
    * scrivere il risultato in un nuovo file *B*.
    
    *A*, *B* e *N* sono parametri che il programma deve acquisire da linea di comando.

    **SOLUZIONE**: `Github <https://github.com/SistemiOperativi/c_examples/tree/main/ex_8_3>`__

  4. Si scriva il codice di una funzione C con la seguente interfaccia :code:`void tunnel(int descriptors[], int count)` tale che, se eseguita, porti l'applicazione a gestire, per ogni file-descriptor dell'array *descriptors* l'inoltro del flusso  dei dati in ingresso verso il canale di standard-output dell'applicazione. Il parametro *count* indica di quanti elementi è costituito l'array *descriptors*. L'inoltro dovrà essere attuato in modo concorrente per i diversi canali. 
  #. Si scriva una funzione C con la seguente interfaccia :code:`void file_check(char *file_name, int num_threads)`. Tale funzione dovrà lanciare num_thread nuovi threads, in modo che ciascuno di essi legga stringhe dallo standard input, e per ogni stringa letta verifichi l'occorrenza di tale stringa all'interno *di ciascuna riga* del file il cui path è identificato tramite il parametro file_name, e stampi la stringa su standard output in caso affermativo.
  #. Scrivere un programma C in cui dato un file *A*, una stringa *B* e un intero *N*, vengano creati *N* thread/processi che cerchino se all'interno del file *A* esiste una linea uguale a *B*.

