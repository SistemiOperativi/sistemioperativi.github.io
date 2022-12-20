7 - Gestione della memoria
""""""""""""""""""""""""""

#. Si consideri il caso di memoria virtuale basata su paginazione a più livelli, indirizzi logici e fisici a N bit, pagine di 4MB e tabelle pari alla dimensione di una pagina. 
   Rispondere alle seguenti domande considerando N pari a 40 bit e 48 bit.

  #. Quanti bit servono per spiazzarsi all'interno di una pagina?
  #. Quanti bit servono per identificare una pagina nel caso di N uguale a 40 bit e 48 bit?
  #. Supponendo di utilizzare un numero di bit per entry in una tabella pari alla minima potenza di 2 necessaria a memorizzare un frame number, quante entry possono essere memorizzate in una tabella?
  #. Quanti livelli sono necessari?
  #. Qual è la struttura dell'indirizzo e l'utilizzo dei bit nel suddetto schema di paginazione?
  #. Qual è il numero massimo di frame di memoria impegnati da un processo nel caso in cui il numero delle tabelle a qualsiasi livello correntemente usate per quel processo in suddetto schema di paginazione sia pari a 10?


2. Data una memoria principale di 4 frame, si determini quanti e quali page fault vengono generati dagli algoritmi FIFO, LRU e Ottimo per la sostituzione delle pagine in sistemi con memoria virtuale data la seguente traccia: 0 9 0 3 5 7 9 0 9 6 7 8 9 7 6 4

  .. container:: toggle

    .. container:: header

      **Mostra/Nascondi Soluzione**

    .. container::

      *FIFO*: #PageFault = 11

      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |**0**|**9**|  0  |**3**|**5**|**7**|  9  |**0**|**9**|**6**|  7  |**8**|  9  |**7**|  6  |**4**|
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  0  |  9  |  9  |  3  |  5  |  7  |  7  |  0  |  9  |  6  |  6  |  8  |  8  |  7  |  7  |  4  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  E  |  0  |  0  |  9  |  3  |  5  |  5  |  7  |  0  |  9  |  9  |  6  |  6  |  8  |  8  |  7  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  E  |  E  |  E  |  0  |  9  |  3  |  3  |  5  |  7  |  0  |  0  |  9  |  9  |  6  |  6  |  8  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  E  |  E  |  E  |  E  |  0  |  9  |  9  |  3  |  5  |  7  |  7  |  0  |  0  |  9  |  9  |  6  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

      *Least-Recently Used*: #PageFault = 10

      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |**0**|**9**|  0  |**3**|**5**|**7**|**9**|**0**|  9  |**6**|  7  |**8**|  9  |  7  |  6  |**4**|
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  0  |  9  |  0  |  3  |  5  |  7  |  9  |  0  |  9  |  6  |  7  |  8  |  9  |  7  |  6  |  4  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  E  |  0  |  9  |  0  |  3  |  5  |  7  |  9  |  0  |  9  |  6  |  7  |  8  |  9  |  7  |  6  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  E  |  E  |  E  |  9  |  0  |  3  |  5  |  7  |  7  |  0  |  9  |  6  |  7  |  8  |  9  |  7  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  E  |  E  |  E  |  E  |  9  |  0  |  3  |  5  |  5  |  7  |  0  |  9  |  6  |  6  |  8  |  9  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+


      *Optimal*: #PageFault = 8

      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |**0**|**9**|  0  |**3**|**5**|**7**|  9  |  0  |  9  |**6**|  7  |**8**|  9  |  7  |  6  |**4**|
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  0  |  0  |  9  |  9  |  9  |  9  |  0  |  9  |  7  |  7  |  9  |  9  |  7  |  6  |  6  |  6  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  E  |  9  |  0  |  0  |  0  |  0  |  9  |  7  |  9  |  9  |  7  |  7  |  6  |  7  |  7  |  7  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  E  |  E  |  E  |  3  |  3  |  7  |  7  |  0  |  0  |  6  |  6  |  6  |  9  |  9  |  9  |  9  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  E  |  E  |  E  |  E  |  5  |  3  |  3  |  3  |  3  |  3  |  3  |  8  |  8  |  8  |  8  |  4  |
      +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+


-----------------


3. Considerando uno schema di paginazione a 3 livelli in cui la tabella di primo livello sia costituita da 4 K elementi, quella di secondo livello da 2 K elementi e quella di terzo livello da 1 K elementi, si determini il numero massimo di pagine gestibili all'interno dello spazio di indirizzamento di un processo.
#. Si consideri una sequenza di generazione di 4 processi, P4, P1, P2 e P3. 
   P1 e P2 hanno taglia 1MB, P3 ha taglia 2 MB e P4 ha taglia 4 MB. Il sistema con multiprogrammazione è caratterizzato da:

   * una memoria di lavoro di 7 MB di cui 1 MB sia riservato per il sistema operativo
   * un meccanismo di allocazione dei processi basato su partizioni dinamiche. 

   Assumendo che P4 non termini prima di P3, si determini quale deve essere la relazione tra il tempo di completamento di P1 e P2 ed il tempo di nascita di P3 affinché, e sotto quali condizioni, ognuno dei 4 processi possa essere correttamente allocato in memoria all'atto della sua creazione. 


   
  .. container:: toggle

    .. container:: header

      **Mostra/Nascondi Soluzione**

    .. container::

      
      +-----++-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  7  ||           | **P2**                |     |                                               |
      +-----++-----+-----+-----+-----+-----+-----+-----+ **P3**                                        +
      |  6  ||     |  **P1**                           |                                               |
      +-----++-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  5  || **P4**                                                                                  |
      +-----++                                                                                         +
      |  4  ||                                                                                         |
      +-----++                                                                                         +
      |  3  ||                                                                                         |
      +-----++                                                                                         +
      |  2  ||                                                                                         |
      +-----++-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      |  1  ||                     **MONITOR**                                                         |
      +-----++-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

      * Siano S_i e T_i rispettivamente l'istante di inizio e terminazione del processo i
      * Vincoli:

        * S_4 < S_1 < S_2 < S_3
        * T_4 > S_3
  
      * Soluzione:
      
        * S_3 > max(T_1, T_2) 
      

.. #. Considera un buddy system. Supponi che le richieste di allocazione siano per porzioni di memoria la cui grandezza sia uniformemente distribuita tra 64bytes e 512Kbytes. Sai stimare mediamente qual è la frazione di memoria che si perde in frammentazione interna ed esterna?

