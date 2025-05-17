# Curs_VCGJ_24_filme

[# DOBRE OCTAVIAN](#dobre-octavian)

[# VASII GABRIEL](#vasii-gabriel)   

[# VASII Gabriel](https://github.com/OctavianT16/Curs_VCGJ_24_filmeoctav/blob/main-Gabriel/README.md)

===================================

# DOBRE OCTAVIAN

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
1. [Descriere versiune](#descriere-versiune)
1. [Configurare](#configurare)
1. [Exemple pagina web](#exemple-pagina-web-octav)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica. pylint - calitate cod](#verificare-statica-cu-pylint)
1. [Reprezentari grafice](#reprezentari-grafice)
1. [Utilizare Docker si containerizare alicatie](https://github.com/crchende/sysinfo/blob/main/doc/dockerdoc.md)
1. [DevOps](#devops-ci)

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

![ruleaza_aplicatia](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/165658515/5d486331-32bd-462a-a00e-3b650eea1c5f)
# EXEMPLE pagina web
<a name="exemple-pagina-web-octav"></a> 

## Pagina principala - ruta default

![index-page](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/165658515/27e3b4a5-2d67-42e7-8cb0-48d280a7df37)

## Pagina Maze Runner

![mazerunner-page](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/165658515/377cb0ce-3923-468d-9ec5-16e860795223)

## Pagina Trailer

![mazerunner-trailer](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/165658515/adc39b5b-1ed5-49c1-97a8-d4fb6417614b)

## Pagina Descriere

![mazerunner-description](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/165658515/1a75be0e-5acf-46da-987b-446688a26a2a)

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

![pytest-mazerunner](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/165658515/af625984-4cd0-4f94-91b6-c5354d98e785)

# Verificare statica cu pylint

[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori

# DevOps CI

[cuprins](#cuprins)
`Continuous Integration` (CI) este o practică de dezvoltare software în care modificările aduse codului sunt integrate frecvent în repository-ul principal. Fiecare integrare este verificată printr-un build automat și prin rularea testelor pentru a detecta rapid eventualele erori. <br>
În cadrul acestei aplicații, pipeline-urile CI sunt configurate pentru Jenkins. Aceste pipeline-uri includ pași pentru clonarea codului, crearea și activarea mediului virtual, rularea testelor cu pytest și verificările statice cu pylint. Aplicația a fost containerizată

## Exemplu executie pipeline Jenkins

![pipeline-jenkins](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/165658515/4e1cc112-27be-45f5-8ef7-873fbadceec0)

## Container Docker

Containerul Docker a fost creat avand numele specificat in stage-ul din pipeline si tag-ul dat de numarul de build

![container-created](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/165658515/8f34ac3a-40ae-4e6e-a5f6-de46d10a5093)

## Push container pe Docker Hub

Containerele create in urma rularii build-urilor au fost incarcate pe DockerHub

![dockerhub](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/165658515/d316f0e9-5c6b-4ee7-8d22-21a1d14aad78)

# Pull Request

Pull Request din branch-ul de dezvoltare catre branch ul protejat main
![pullrq](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/165658515/899a9b95-71e0-493a-be4c-7d17ccd2618b)

# Bibliografie:

[cuprins](#cuprins)

- [Github Actions](https://docs.github.com/en/actions)

# VASII GABRIEL
[Exemple pagina web](#exemple-pagina-web-gabi)



# Testare Jenkins

![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/155522811/f6702a3c-8680-4109-9576-838b5d4d2098)

![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/155522811/6067dacb-a3a3-4c09-916b-4d94514d6bff)

# Aplicatie main.py (Film Godzilla) containerizata
# EXEMPLE pagina web
<a name="exemple-pagina-web-gabi"></a>
![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/155522811/4ebef2d9-7c45-411e-96fd-d8b8fc1cd81e)
![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/155522811/071f349e-97ae-460e-b007-992f84196a70)
![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/155522811/c79f41ac-b4b3-41ff-9003-8d8d147773a6)
