7 - File management
"""""""""""""""""""

#. Si consideri un file system con allocazione a catena ed accesso indicizzato. Dato un file:

  * contente 1M record;
  * il relativo indice ha taglia pari a 512 record e contiene 128 chiavi uniformemente distribuite nel file;
  * memorizzato su un dispositvo di massa, la cui taglia di un blocco è pari a 4096 record. 
  
  Calcolare la latenza massima e minima considerando che:

  * il tempo medio di accesso ad un blocco è 10ms;
  * l'accesso ad una chiave dell'indice in ram è pari a 1ms.


2. Si consideri un file system con allocazione indicizzata ospitato su un dispositivo i cui blocchi hanno taglia pari a 1024 record e un riferimento a blocco occupa 8 record. Il record di sistema ha:
  
  * 128 entry per acesso diretto;
  * 4 entry per accesso indiretto;
  * 4 entry per accesso doppiamente indiretto.
  
  Qual è la taglia massima di un file in record? 

3. Si consideri inoltre senario dove un processo P apra un file F (attualmente non in uso da parte di alcun processo) e poi esegua 2 fork(). Indicare il numero delle sessioni di I/O verso  il file F a valle dell’esecusione delle 2 fork() da parte di P.
#. Si consideri un dispositivo di memoria di massa con blocchi di taglia pari a 4 KB, indici di blocchi di taglia pari a 4 byte, ed un record di sistema contenente in totale 12 indici di cui N diretti ed M indiretti. Si determini il valore di N ed M, qualora esista, che possa permettere di allocare file di taglia almeno pari a 4 GB.
#. Si supponga di avere un file system che supporta il metodo di allocazione a catena. Si supponga inoltre che il dispositivo di memoria di massa ove il file system è ospitato abbia blocchi di taglia pari a 4 K record, e che un indice (puntatore) di blocco di dispositivo sia espresso con 16 record. Si supponga inoltre di avere un file F di taglia pari a 16 M record. Si calcoli il numero di blocchi necessari ad allocare il file sul dispositivo di memoria di massa secondo lo schema a catena.