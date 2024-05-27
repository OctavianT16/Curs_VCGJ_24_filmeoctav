# Curs_VCGJ_24_filme

===================================

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
1. [Descriere versiune](#descriere-versiune)
1. [Configurare](#configurare)
1. [Exemple pagina web](#exemple-pagina-web)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica. pylint - calitate cod](#verificare-statica-cu-pylint)
1. [Reprezentari grafice](#reprezentari-grafice)
1. [Utilizare Docker si containerizare alicatie](https://github.com/crchende/sysinfo/blob/main/doc/dockerdoc.md)
1. [DevOps](#devops-ci)
   1. [Pipeline Jenkins](#exemplu-executie-pipeline-jenkins)
   1. [Workflow GitHub Actions](#exemplu-executie-workflow-in-github-actions)
1. [Bibliografie](#bibliografie)

# Descriere aplicatie

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru o parte din functiile din biblioteca aplicatiei, aflate in directorul `app/lib`.

`DevOps CI`.
Pipeline-ul pentru Jenkins este definint in fisierul `Jenkinsfile`.
Worflow-ul (pipeline-ul) pentru GitHub Actions, in fisierul `.github/workflows/sysinfo_test.yml`.

Ambele pipeline-uri cloneaza codul, creaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).

Aplicația "Maze Runner Info" este un instrument simplu și eficient pentru a obține informații detaliate despre filmul "Maze Runner". Utilizând framework-ul Flask pentru componenta web, aplicația permite utilizatorilor să acceseze rapid și ușor datele despre filmul ales.

Funcționalitățile principale includ:

- _**Informații esențiale despre film**_:
  Pagina principală oferă un rezumat al filmului "Maze Runner", inclusiv descrierea filmului, trailer-ul oficial și alte informații cheie, cum ar fi regizorul, actorii principali, data lansării și genul filmului.
- _**Navigare intuitivă**_:
  Interfața aplicației este simplă: pagina principală conține link-uri către paginile specifice, iar fiecare pagină specifică conține un link înapoi la pagina principală.
- **_Suport pentru afișarea grafică_**:
  Pentru a oferi o experiență vizuală plăcută, aplicația include stilizarea cu `CSS`. Acest exemplu demonstrează modul în care aplicația poate prezenta datele într-un mod atrăgător și ușor de înțeles, prin intermediul designului și al aspectului vizual al paginilor web.
- **_Containerizare simplă_**:
  Aplicația include suport pentru containerizare folosind un fișier Dockerfile, facilitând implementarea și distribuirea pe diferite platforme și medii de execuție.

- **_Testare automată_**: Aplicația include unit testing cu pytest și verificări statice cu pylint.
- **_DevOps CI_**: Pipeline-ul pentru Jenkins este definit într-un fișier `Jenkinsfile`.

# Descriere versiune

- ruta standard '/' - URL: http://127.0.0.1:5011
- rute in aplicatia WEB pentru:
  - pagina principala: '/mazerunner' - URL: 'http://127.0.0.1:5011/mazerunner',
  - descriere: '/mazerunner/description' - .../mazerunner/description
  - trailer: '/mazerunner/trailer' - .../mazerunner/trailer

# Configurare

[cuprins](#cuprins)

Clonare repository

Creati spatiul de lucru si clonati aplicatia filme:

```text
   mkdir filme_scc
   cd filme_scc
   git clone https://github.com/Raluca93/Curs_VCGJ_24_filme.git

   ********
   NOTA: INSTALARE dependinte (cu apt)

   sudo apt upgrade
   sudo apt install net-tools
   sudo apt install git
   sudo apt install python3
   sudo apt install python3-pip
   sudo apt install python3.10-venv

   cd filme_scc

   git checkout <branch_dorit>

```

Configurare .venv si instalare pachete

In directorul 'filme_scc' rulati comenzile:

1. activeaza_venv: Incearca sa activeze venv-ul.
   Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask si flask-bootstrap.
   La urmatoarea rulare, va activa doar venv-ul.
2. ruleaza_aplicatia: De rulat doar dupa activarea venv-ului.
   Va porni serverul pe IP: 127.0.0.1 si port: 5011.
   Acces server din browser: http://127.0.0.1:5011

# EXEMPLU activare venv si rulare

```text
octavian@Ubuntu22:~/filme_scc$ . ./activeaza_venv
SUCCESS: venv was activated.
(.venv) octavian@Ubuntu22:~/filme_scc$ . ./ruleaza_aplicatia
filme
 * Serving Flask app 'filme'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5011
Press CTRL+C to quit
 * Restarting with stat
filme
```

![ruleaza_aplicatia](https://github.com/OctavianT16/Curs_VCGJ_24_filmeoctav/assets/165658515/e1f5e589-9509-482b-8d16-77303d77d91b)

# EXEMPLE pagina web

## Pagina principala - ruta default

![index-page](https://github.com/OctavianT16/Curs_VCGJ_24_filmeoctav/assets/165658515/5f60d0f9-47ea-40b1-ab75-4594db135a17)

## Pagina Maze Runner

![mazerunner-page](https://github.com/OctavianT16/Curs_VCGJ_24_filmeoctav/assets/165658515/0c502f45-fea4-4861-b5cb-ad9e7f0c2e70)

## Pagina Trailer

![mazerunner-trailer](https://github.com/OctavianT16/Curs_VCGJ_24_filmeoctav/assets/165658515/deecb2a1-dfd0-4e04-b2d4-d6ca6b9840f4)

## Pagina Descriere

![mazerunner-description](https://github.com/OctavianT16/Curs_VCGJ_24_filmeoctav/assets/165658515/39427e05-1aa2-4de8-8aa2-72d63020dd48)

# Testare cu pytest

[cuprins](#cuprins)

Aplicația "Maze Runner Info" include teste unitare și de integrare pentru a asigura funcționalitatea și calitatea componentelor. Testele sunt realizate folosind pachetul pytest și se concentrează pe verificarea stării și conținutului răspunsurilor HTTP, precum și pe încărcarea corectă a resurselor statice.

## Teste pentru componente specifice

- **Testul trailer-ului** <br><br>
  Fișierul test_filme.py conține teste pentru pagina de trailer a filmului "Maze Runner", respectiv pentru fișierul de stil CSS utilizat de aplicație.<br>
  Testul `test_incarcare_trailer` verifică dacă pagina se încarcă corect și dacă include link-ul corect către videoclipul trailer-ului de pe YouTube.<br>

### **Functionalitate test trailer:**

- Trimite o cerere GET către /mazerunner/trailer.
- Verifică dacă răspunsul HTTP are codul de stare 200 OK.
- Verifică prezența link-ului video YouTube în datele răspunsului.

Testul `test_style_css` verifică dacă fișierul style.css se încarcă corect și returnează codul de stare așteptat.

### **Functionalitate test style.css:**

- Trimite o cerere GET către /static/style.css.
- Verifică dacă răspunsul HTTP are codul de stare 200 OK.
- Verifica prezența imaginii de fundal a paginii principale

Pentru testare s-a folosit pachetul pytest din python. Acesta se afla in lista de pachete care trebuie instalate, in fisierul quickrequirements.txt.

![pytest-mazerunner](https://github.com/OctavianT16/Curs_VCGJ_24_filmeoctav/assets/165658515/e02f2aea-a64e-4c26-a3ac-2e02ecb94190)

# Verificare statica cu pylint

[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori

# DevOps CI

[cuprins](#cuprins)
`Continuous Integration` (CI) este o practică de dezvoltare software în care modificările aduse codului sunt integrate frecvent în repository-ul principal. Fiecare integrare este verificată printr-un build automat și prin rularea testelor pentru a detecta rapid eventualele erori. <br>
În cadrul acestei aplicații, pipeline-urile CI sunt configurate pentru Jenkins. Aceste pipeline-uri includ pași pentru clonarea codului, crearea și activarea mediului virtual, rularea testelor cu pytest și verificările statice cu pylint. Aplicația a fost containerizată

## Exemplu executie pipeline Jenkins

![image](https://github.com/crchende/sysinfo/assets/57460107/8fdaa372-44ee-409b-855c-053e78baf800)

# Bibliografie:

[cuprins](#cuprins)

- [Github Actions](https://docs.github.com/en/actions)
