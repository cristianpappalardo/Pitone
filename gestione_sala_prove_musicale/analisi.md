# GESTIONE SALA PROVE MUSICALI

## Divisione dei file

Il progetto prevede la suddivisione in file. Ogni file ha una funzione diversa:

- clienti.py classe cliente.

- sale.py classe sale.

- prenotazione.py classe prenotazione.

- service.py che gestisce la logica.

- dump.py crea il database.


## Database

### Clienti:
    - cliente_id int primary key
    - nome_gruppo TEXT
    - nome_referente TEXT
    - cell INT
    - email TEXT


### Sale

    - sale_id int primary key
    - prenotazione TEXT 


### Prenotazioni

    - prenotazione_id int primary key
    - cliente_id int not null
    - sale_id int not null
    - inizio_prenotazione text
    - fine_prenotazione text
    - foreign key (cliente_id) references cliente(cliente_id)
    - foreign key (sale_id) references sale(sale_id)
    
