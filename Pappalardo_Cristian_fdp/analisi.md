## ANALISI DEL PROBLEMA

Il progetto ha l'obbiettivo di realizzare un gestionale per le aule studio ITS. Il sistema deve prevedere la suddivisione in modelli per la gestione delle classi, servizi per la logica applicativa, un file dump per le creazione del database e un file main che permette di gestire il tutto tramite l'interazione di un menù testuale.

### Le entita centrali del dominio sono:

- Studenti: rappresenta gli studenti che utilizzano le aule studio. Devono possedere delle informazioni anagrafiche.

- Aule studio: rappresenta le aule studio utilizzate dagli studenti. Deve possedere un numero massimo di posti disponibili e un nome.

- Prenotazioni: rappresenta le prenotazioni delle aule da parte di uno studente.


### Dal punto di vista operativo, il software deve consentire:

- Inserimento e visualizzazione degli studenti presenti in anagrafica.
- Inserimento di nuove aule studio.
- Aggiornamento della capacità di un'aula studio quando viene prenotata o quando viene cancellata una prenotazione.
- Eliminazione di un'aula studio quando non più necessarie.
- Creazione di una nuova prenotazione tra uno studente e un'aula studio.
- Rimozione di una prenotazione esistente, con conseguente aggiornamento dei posti disponibili dell'aula


### I vincoli logici 

- Un studente puo avere al massimo una prenotazione attiva.
- Non è possibile prenotare un'aula che ha raggiunto il limite di posti disponibili.
- La rimozione di un'assegnazione deve riportare il numero di posti disponibili allo stato precedente.

### Requisiti tecnici

- Modelli a oggetti: definiscono le classi del dominio (Studente, Aula Studio, Prenotazione) e le loro proprieta.
- Servizi applicativi: implementano la logica di business e i controlli sui vincoli prima di operare sul database.
- Menu testuale: gestisce l'interazione con l'utente, raccoglie input e invoca i servizi.
- Script di inizializzazione database: crea tabelle e relazioni SQLite necessarie al funzionamento.
- Prevedere nel dump anche il caricamento di un’aula con nome “Dummy” per cui, per un guasto, i posti disponibili saranno 5 in meno di quelli dichiarati sul database (prevedere questa gestione nel codice)

### Istruzioni non viste

- conn.rollback():
    riporta il database allo stato precedente all'inizio della transazione, annullando tutte le modifiche effettuate durante la transazione stessa. Viene utilizzato per gestire errori o situazioni impreviste che potrebbero verificarsi durante l'esecuzione di operazioni sul database, garantendo l'integrità dei dati.
- raise exception:
    mostra un messaggio di errore e interrompe l'esecuzione del programma. Viene utilizzato per segnalare situazioni anomale o errori che si verificano durante l'esecuzione del codice, consentendo di gestire tali situazioni in modo appropriato.