## Analisi del problema

Il progetto ha l'obiettivo di realizzare un'applicazione gestionale per il parcheggio aziendale, in grado di organizzare in modo ordinato i posti auto assegnati ai dipendenti. Il sistema deve evitare errori manuali, sovrapposizioni e assegnazioni incoerenti, offrendo un flusso operativo semplice tramite menu testuale.

L'applicazione si basa su tre aree funzionali principali: gestione dei dipendenti, gestione dei posti auto e gestione delle assegnazioni. Tutti i dati devono essere persistenti, quindi memorizzati in un database SQLite locale. La scelta di SQLite consente di avere un archivio strutturato e interrogabile senza dipendenze esterne complesse.

Le entita centrali del dominio sono:

- Dipendente: rappresenta una persona registrata nell'anagrafica aziendale. Ogni dipendente deve avere un identificativo univoco e i dati minimi richiesti dal sistema (ad esempio nome, cognome o altri campi stabiliti in fase di implementazione).
- Posto auto: rappresenta un singolo stallo del parcheggio. Ogni posto ha un identificativo univoco e uno stato operativo (disponibile o assegnato).
- Assegnazione: rappresenta il legame tra dipendente e posto auto. Questa entita collega in modo esplicito i due elementi e permette di tracciare quali posti risultano occupati e da chi.

Dal punto di vista operativo, il software deve consentire:

- Inserimento e visualizzazione dei dipendenti presenti in anagrafica.
- Inserimento di nuovi posti auto.
- Aggiornamento dello stato di un posto auto quando viene assegnato o liberato.
- Eliminazione di un posto auto quando non e piu utilizzabile o non fa piu parte del parcheggio.
- Creazione di una nuova assegnazione tra un dipendente e un posto disponibile.
- Rimozione di un'assegnazione esistente, con conseguente liberazione del posto.

I vincoli logici sono il cuore del problema e devono essere controllati sia a livello applicativo sia, dove possibile, a livello database:

- Un dipendente puo avere al massimo un posto auto.
- Un posto auto puo essere assegnato a un solo dipendente.
- Non devono esistere assegnazioni duplicate.
- Non e possibile assegnare un posto gia occupato.
- La rimozione di un'assegnazione deve riportare il posto allo stato disponibile.

Per rispettare i requisiti tecnici e mantenere il codice ordinato, il progetto deve essere strutturato in livelli separati:

- Modelli a oggetti: definiscono le classi del dominio (Dipendente, PostoAuto, Assegnazione) e le loro proprieta.
- Servizi applicativi: implementano la logica di business e i controlli sui vincoli prima di operare sul database.
- Menu testuale: gestisce l'interazione con l'utente, raccoglie input e invoca i servizi.
- Script di inizializzazione database: crea tabelle e relazioni SQLite necessarie al funzionamento.
