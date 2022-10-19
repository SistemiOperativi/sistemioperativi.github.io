2- Processi e thread
""""""""""""""""""""

1. Scrivere un programma in C che:
 
   * prende inizialmente una stringa da input (può contenere anche spazi bianchi) e la salva in un buffer
   * fork-a un processo figlio che manda in stampa la stessa stringa acquisita dal processo padre.
   * Il processo padre termina solo dopo che il processo figlio ha terminato (verificare che tale ordine è rispettato stampando i PID dei processi).

2. Scrivere un programma in C che:
 
  * prende inizialmente una stringa da input (può contenere anche spazi bianchi) e la salva in un buffer
  * fork-are 2 processi figli che contribuiscono a stampare la stringa inversa della stringa acquisita dal processo padre.
  * Il processo padre termina solo dopo che i processi figli hanno terminato.

3. Scrivere un programma in C che:
 
  * prende inizialmente N (a piacere) stringhe rappresentanti N directory corrette
  * fork-a quindi N processi che andranno ad eseguire il comando ls su una directory differente.
  * Il processo padre termina dopo i processi figli