��    	      d               �   '   �      �   &   �   G        L  ~  f  �   �  �   �  �  �  +        G  %   P  5   v     �  v  �  �   ?  �   	   Cosa stampano le righe 18, 36, 42 e 46? Domanda Il programma è diviso in due sezioni: La variabile :code:`global_var` viene stampata 4 volte, rispettivamente PVST - Processi vs Thread Processi vs Thread (:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/pvst/pvst.c">PVST</a> <a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/pvst/pvst.c"></a>`) è un programma C il cui scopo è quello di evidenziare differenze basilari tra processi e thread. il main thread crea un processo child secondo lo schema proposto in :doc:`FEW <few>`. Entrambi i processi scrivono sulla variabile globale :code:`global_var` e successivamente ne stampano il valore su standard output. il main thread crea un thread child secondo lo schema proposto in :doc:`PFEW <pfew>`. Entrambi i thread scrivono sulla variabile globale :code:`global_var` e successivamente ne stampano il valore su standard output. Project-Id-Version: Sistemi Operativi 
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2021-11-21 23:51+0100
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: en
Language-Team: en <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.9.1
 What is printed at lines 18, 36, 42 and 46? Question The program consists in two sections: The variable :code:`global_var` will printed 4 times: PVST - Processes vs Threads Processes vs Threads (:raw-html:`<a class="external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/pvst/pvst.c">PVST</a> <a class="fa fa-github external" target="_blank" href="https://github.com/SistemiOperativi/c_examples/blob/main/pvst/pvst.c"></a>`) it is a C program C that shows the main differences when creating processes and threads. the main thread creates a child process according to the scheme shown in :doc:`FEW <pfew>`. Both processes write on a global variable :code:`global_var` and print its value on standard output.  the main thread creates a child thread according to the scheme shown in :doc:`PFEW <pfew>`. Both threads write on a global variable :code:`global_var` and print its value on standard output.  