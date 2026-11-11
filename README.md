# UDP Flooder - Script a Scopo Didattico

Questo repository contiene uno script Python (`udp_flooder.py`) ideato per illustrare il funzionamento di base dei pacchetti UDP (User Datagram Protocol) e mostrare come si comporta un attacco di tipo **UDP Flooding** su rete locale.

## ⚠️ Disclaimer e Uso Consentito

> **ATTENZIONE:** Questo progetto è stato sviluppato **ESCLUSIVAMENTE A SCOPO EDUCATIVO E DIDATTICO**.
> 
> * **È severamente vietato** l'utilizzo di questo script al di fuori di ambienti di laboratorio privati, isolati e di proprietà dell'utente (o su reti per le quali si possiede un'autorizzazione scritta ed esplicita).
> * L'uso non autorizzato di strumenti di stress test o flood su reti altrui o pubbliche costituisce un reato informatico sanzionabile dalla legge.
> * L'autore non si assume alcuna responsabilità per eventuali danni, interruzioni di servizio o utilizzi illeciti derivanti dall'uso di questo codice.

---

## 📌 Descrizione dello Script

Lo script `udp_flooder.py` effettua le seguenti operazioni:

1. Richiede all'utente l'indirizzo IP target e la porta di destinazione.
2. Inizializza un socket UDP non orientato alla connessione (`socket.SOCK_DGRAM`).
3. Chiede il numero di pacchetti che l'utente intende inviare (controllando che l'input sia valido).
4. Genera per ciascun pacchetto un payload casuale di dimensione fissa par ad **1 KB** (1024 byte).
5. Invia i pacchetti al target e gestisce le eventuali interruzioni da tastiera (`Ctrl+C`) o errori di rete, chiudendo correttamente il socket al termine.

---

## 🛠️ Requisiti

* **Python 3.x**
* Nessuna libreria esterna richiesta (utilizza esclusivamente i moduli standard `socket` e `random`).

---

## 🚀 Come Utilizzare lo Script

1. **Clona il repository** o scarica il file:
   ```bash
   git clone https://github.com/tuo-username/tuo-repository.git
   cd tuo-repository
   ```

2. **Esegui lo script**:
   ```bash
   python udp_flooder.py
   ```

3. **Inserisci i parametri richiesti** a terminale:
   * **Target IP**: Indirizzo IP della macchina di test (es. `127.0.0.1` o IP del proprio laboratorio).
   * **Target Port**: Porta di destinazione (compresa tra 1 e 65535).
   * **Numero di pacchetti**: Quantità di pacchetti da inviare.

---

## 🧪 Ambiente di Test Consigliato

Per testare lo script in sicurezza:
* Utilizza l'interfaccia di loopback locale (`127.0.0.1`).
* Configura una macchina virtuale (es. con VirtualBox o VMware) impostata su una rete **Internal Network** o **Host-Only**.
* Analizza il traffico generato utilizzando strumenti di packet capture come **Wireshark**.