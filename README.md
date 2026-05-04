# README (EST)

# WebFile Server

Lihtne veebipõhine failiserver koos tagide süsteemi ja kasutajakontodega.

Projekt on loodud lõputöö raames erialal Tööstusinformaatika.

---

# 📌 Projekti kirjeldus

WebFile Server on veebirakendus failide salvestamiseks, haldamiseks ja otsimiseks brauseri kaudu.

Projekti peamised eesmärgid:

* luua mugav failihaldussüsteem;
* realiseerida tagide süsteem;
* luua File Explorer / Pinterest stiilis kasutajaliides;
* valmistada ette alus tulevasele desktop-rakendusele;
* realiseerida REST API teenuste vaheliseks suhtluseks.

Praeguses etapis on projekt õppeprototüüp, mis liikus alpha 0.0.8 versioonist beta 0.1.0 versioonile.

---

# ⚙️ Kasutatavad tehnoloogiad

## Backend

* Python
* Flask
* SQLite
* REST API

## Frontend

* HTML
* CSS
* JavaScript

## Linux / Server

* Ubuntu
* BIND9
* DHCP
* NTP (chrony)

---

# ✨ Realiseeritud funktsioonid

* kasutajate registreerimine ja autentimine;
* failide üleslaadimine;
* avalikud ja privaatsed failid;
* failide hoidmine kasutajate kaustades;
* tagide süsteem;
* failide otsing tagide järgi;
* piltide kuvamine;
* failiinfo muutmine;
* REST API;
* töö lokaalses võrgus.

---

# 🔮 Tulevased võimalused

* tagide automaatne soovitamine;
* drag & drop;
* Docker;
* MySQL/PostgreSQL;
* desktop-rakendus;
* õiguste ja rollide süsteem;
* mitmekeelsus;
* failide krüpteerimine;
* WebSocket teavitused;
* P2P failiedastus.

---

# 🗂️ Projekti struktuur

```bash
file_server/
│
├── app.py
├── database.db
├── uploads/
│
├── templates/
│   ├── index.html
│   └── login.html
│
├── static/
│   ├── style.css
│   └── javascript.js
│
└── venv/
```

---

# 🚀 Paigaldamine

## Süsteemi uuendamine

```bash
sudo apt update
```

## Python paigaldamine

```bash
sudo apt install python3 python3-pip python3.12-venv
```

## Virtuaalkeskkonna loomine

```bash
python3 -m venv venv
```

## Virtuaalkeskkonna aktiveerimine

```bash
source venv/bin/activate
```

## Flask paigaldamine

```bash
pip install flask
```

---

# ▶️ Käivitamine

```bash
python3 app.py
```

Pärast käivitamist on veebileht saadaval aadressil:

```txt
http://127.0.0.1:5000
```

---

# 🔐 Turvalisus

Realiseeritud:

* paroolide hashimine;
* avalike ja privaatsete failide eraldamine;
* teiste kasutajate failide muutmise piiramine.

Planeeritud:

* JWT;
* HTTPS;
* DoS kaitse;
* CSRF kaitse;
* Docker isolation.

---

# 📁 Failide salvestamine

```bash
uploads/
└── username/
    ├── images/
    ├── videos/
    └── other/
```

---

# 🏷️ Tagide süsteem

Iga fail võib sisaldada:

* tage;
* kirjeldust;
* loomise kuupäeva;
* faili nime.

Tagisid kasutatakse:

* otsinguks;
* filtreerimiseks;
* failide sorteerimiseks.

---

# 📌 Projekti staatus

🟡 Beta 0.1.0

Õppeprojekt lõputöö jaoks.

---

# 👨‍💻 Autor

Noralik
