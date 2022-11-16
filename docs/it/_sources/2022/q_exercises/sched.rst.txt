3 - Scheduling
""""""""""""""


#. Si consideri uno scenario con 4 processi {P1,..., P4} CPU-bound e generati in sequenza a partire da P1 a P4 con ritardi trascurabili. 
  Il processo Pi richiede 1/i secondi di CPU per completare la propria esecuzione.
  Considerando che il ritardo di context-switch sia trascurabile e che RR abbia una time slice pari a 125ms, si calcoli per gli algoritmi FCFS, SPN e RR il tempo di primo accesso alla CPU e il tempo di completamento per ciascun processo.

    .. container:: toggle

      .. container:: header

        **Mostra/Nascondi Soluzione**

      .. container::

        *FCFS*: 

        +---------+----+----+----+----+----+----+----+----+----+----+----+----+------+----+
        |process  | P1                                    |    P2             |  P3  | P4 |
        +---------+----+----+----+----+----+----+----+----+----+----+----+----+------+----+
        | CPU     |                                       |                   |      |    |
        + Release +1.00                                   + 1.5               + 1.83 +2.08+ 
        | Time    |                                       |                   |      |    |
        +---------+----+----+----+----+----+----+----+----+----+----+----+----+------+----+
        
        +----------+---------------+---------------+
        | Processo | Primo Accesso | Completamento |
        +----------+---------------+---------------+
        | P1       |  0            |   1           |
        +----------+---------------+---------------+
        | P2       |  1            |   1.5         |
        +----------+---------------+---------------+
        | P3       |  1.5          |   1.83        |
        +----------+---------------+---------------+
        | P4       |  1.83         |   2.08        |
        +----------+---------------+---------------+

        *SPN*: 

        Assunzione 1: Lo scheduler viene attivato dopo l'arrivo di tutti i processi

        +---------+----+------+----+----+----+----+----+----+----+----+----+----+----+----+
        |process  | P4 |  P3  |    P2             | P1                                    |
        +---------+----+------+----+----+----+----+----+----+----+----+----+----+----+----+
        | CPU     |    |      |                   |                                       |
        + Release +0.25+ 0.58 +  1.08             +  2.08                                 + 
        | Time    |    |      |                   |                                       |
        +---------+----+------+----+----+----+----+----+----+----+----+----+----+----+----+
        
        +----------+---------------+---------------+
        | Processo | Primo Accesso | Completamento |
        +----------+---------------+---------------+
        | P1       |  1.08         |   2.08        |
        +----------+---------------+---------------+
        | P2       |  0.58         |   1.08        |
        +----------+---------------+---------------+
        | P3       |  0.25         |   0.58        |
        +----------+---------------+---------------+
        | P4       |  0            |   0.25        |
        +----------+---------------+---------------+


        Assunzione 2: Lo scheduler è attivato all'arrivo del primo processo 

        +---------+----+----+----+----+----+----+----+----+----+------+----+----+----+----+
        |process  | P1                                    | P4 |  P3  |    P2             |
        +---------+----+----+----+----+----+----+----+----+----+------+----+----+----+----+
        | CPU     |                                       |    |      |                   |
        + Release +1.00                                   +1.25+ 1.58 +2.08               +          
        | Time    |                                       |    |      |                   |
        +---------+----+----+----+----+----+----+----+----+----+------+----+----+----+----+
        
        +----------+---------------+---------------+
        | Processo | Primo Accesso | Completamento |
        +----------+---------------+---------------+
        | P1       |  0            |   1           |
        +----------+---------------+---------------+
        | P2       |  1.58         |   2.08        |
        +----------+---------------+---------------+
        | P3       |  1.25         |   1.58        |
        +----------+---------------+---------------+
        | P4       |  1            |   1.25        |
        +----------+---------------+---------------+

        *RR*: 

        +---------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
        |process  | P1  | P2  | P3  | P4  | P1  | P2  | P3  | P4  | P1  | P2  | P3  | P1  | P2  | P1  | P1  | P1  | P1  |
        +---------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
        | CPU     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
        + Release +0.125+0.250+0.375+0.500+0.625+0.750+0.875+1.000+1.125+1.250+1.333+1.458+1.583+2.083+     +     +     +
        | Time    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
        +---------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
        
        

        +----------+---------------+---------------+
        | Processo | Primo Accesso | Completamento |
        +----------+---------------+---------------+
        | P1       |  0.000        |   2.08        |
        +----------+---------------+---------------+
        | P2       |  0.125        |   1.58        |
        +----------+---------------+---------------+
        | P3       |  0.250        |   1.33        |
        +----------+---------------+---------------+
        | P4       |  0.375        |   1.00        |
        +----------+---------------+---------------+

  --------------------------

2. Si consideri uno scenario in cui uno scheduler Multilevel-feedback queue abbia 4 livelli di priorità, ed in cui il quanto di tempo assegnato ai processi al livello i sia di 1/2^i millisecondi. Si supponga che all'istante T0 nascano 2 processi A e B, entrambi CPU-bound. Il processo B richiede 10 millisecondi di tempo di CPU per completare la sua esecuzione. Si identifichi la durata massima (in termini di tempo di CPU) del processo A affinché il processo B possa completare la sua esecuzione entro il tempo T0+17 nei due casi in cui il primo processo ad essere schedulato in CPU sia A oppure B. Si supponga che il tempo di CPU per i context switch e per l'esecuzione dello scheduler sia nullo.
#. Si consideri uno scenario in cui al tempo T0 nasca un processo P0 puramente CPU-bound di durata (tempo di CPU) pari a 10 secondi ed al tempo T0 + 3 secondi P0 origini un altro processo P1 puramente CPU-bound di durata (tempo di CPU) pari a 6 secondi. Supponendo che le durate dei processi siano note al tempo della loro generazione, e che il tempo di CPU per eseguire uno scheduler sia trascurabile. si calcoli il tempo massimo di completamento del processo P1 nel caso in cui il sistema abbia come scheduler Shortest Process Next oppure Shortest-Remaining-Time Next.