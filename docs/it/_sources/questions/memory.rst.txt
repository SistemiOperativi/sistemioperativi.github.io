:orphan:

5 - Gestione della memoria
""""""""""""""""""""""""""

.. comment 
    #. Descrivi la paginazione e la segmentazione mostrando vantaggi e svantaggi di ciascuna.
    #. Mostra lo schema di paginazione a due livelli e il processo di traduzione di un indirizzo virtuale in fisico. Quali sono i vantaggi e gli svantaggi nell'uso di tale schema?
    #. Cosa è e a cosa serve il translation lookside buffer?
    #. Mostrare uno schema di segmentazione paginata con TLB e descriverne il funzionamento per la traduzione da indirizzo logico a fisico.
    #. Che cosa è un buddy system?
    #. Descrivi l'anomalia di Belady.
    #. Descrivere l'algoritmo dell'orologio nell'ambito delle politiche di replacement delle pagine.
    #. Descrivere gli aspetti principali di gestione della memoria virtuale.
    #. Descrizione la gestione di un page fault nel caso di memoria virtuale basata su paginazione.
    #. Descrivere le caratteristiche delle politiche di gestione del resident set di processo.
    #. Descrivere il fenomeno del thrashing nel contesto della memoria virtuale.
    #. Descrivere la tecnica di gestione delle memoria basata su partizioni dinamiche, indicando anche di quali supporti per il binding degli indirizzi questa necessita.
    #. Descrivere l'algoritmo di selezione Least-Recently-Used (LRU) per sistemi di memoria virtuale basati su paginazione. 
    #. Si descriva la tecnica della paginazione, indicando quali siano le strutture dati fondamentali che un sistema operativo deve gestire per metterla in atto.
    #. Descrivere l'algoritmo ottimo per la sostituzione delle pagine in ambiente di memoria virtuale. Si indichi infine se tale algoritmo soffra o meno dell'anomalia di Belady, motivando la risposta.
    #. Descrivere la struttura e l'utilizzo della tabella delle pagine e la relazione tra questa ed i componenti hardware presenti su una architettura di processore convenzionale.

    .. #. Considera un buddy system. Supponi che le richieste di allocazione siano per porzioni di memoria la cui grandezza sia uniformemente distribuita tra 64bytes e 512Kbytes. Sai stimare mediamente qual è la frazione di memoria che si perde in frammentazione interna ed esterna?

