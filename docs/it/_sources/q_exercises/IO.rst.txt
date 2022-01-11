6 - I/O Management
""""""""""""""""""

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