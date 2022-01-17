5 - Gestione della memoria
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
#. Considerando uno schema di paginazione a 3 livelli in cui la tabella di primo livello sia costituita da 4 K elementi, quella di secondo livello da 2 K elementi e quella di terzo livello da 1 K elementi, si determini il numero massimo di pagine gestibili all’interno dello spazio di indirizzamento di un processo.
#. Si consideri una sequenza di generazione di 4 processi, P4, P1, P2 e P3. 
   P1 e P2 hanno taglia 1MB, P3 ha taglia 2 MB e P4 ha taglia 4 MB. Il sistema con multiprogrammazione è caratterizzato da una memoria di lavoro di 7 MB di cui 1 MB sia riservato per il sistema operativo, un meccanismo di allocazione dei processi basato su partizioni dinamiche. Assumendo che P4 non termini prima di P3, si determini quale deve essere la relazione tra il tempo di completamento di P1 e P2 ed il tempo di nascita di P3 affinchè, e sotto quali condizioni, ognuno dei 4 processi posssa essere correttamente allocato in memoria all’atto della sua creazione. 


.. #. Considera un buddy system. Supponi che le richieste di allocazione siano per porzioni di memoria la cui grandezza sia uniformemente distribuita tra 64bytes e 512Kbytes. Sai stimare mediamente qual è la frazione di memoria che si perde in frammentazione interna ed esterna?

