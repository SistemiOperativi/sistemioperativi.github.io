3 - Sincronizzazione
""""""""""""""""""""

#. Una applicazione ha *p* thread produttori e *c* thread consumatori. L'applicazione lavora in due fasi.
   Nella prima fase i thread produttori *Pi* inseriscono in una coda vuota *c* elementi.
   Nella seconda fase i thread consumatori *Ci* estraggono ciascuno un elemento dalla coda a partire da *C1* a *Cc*.
   Le due fasi si alternano per un tempo infinito.
   Scrivere in pseudocodice il corpo delle funzioni eseguite da un generico thread *Pi* e *Ci* assumendo che:
   
   * la coda è inizialmente vuota;
   * l'implementazione disponibile della coda NON è thread safe;
   * è ammesso solo l'utilizzo di semafori;
   * non è ammesso utilizzare altre variabili condivise ad eccezione di eventuali semafori e della coda.

  