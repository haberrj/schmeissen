# Schmeissen

__READ THE [CONTRIBUTING](docs/CONTRIBUTING.md) DOC.__

This app was created for the card game Schmeißen, Ziehen, Liegen (that we got 
to know from the German people in South-East Asia). The idea is to create this 
app as an online game so we can play in the quarantine.

The app would have the ability to reside on a server and this repo will be our 
space to develop the app.

### Codebase

#### Technologies

-   ```Flask``` web framework
-   ```Flask-SocketIO``` websockets for bi-directional data flow
-   ```Flask-SQLAlchemy``` ORM
-   ```gunicorn``` WSGI
-   ```SQLite``` development database
-   ```MySQL``` production database

### Notes

-   Start with barebones app (only one game-session server for us).
-   I'm not updating shit in german.

## Deutsche

Dieses App wurde fürs Kartespiel Schmeißen, Ziehen, Liegen (dass wir von den 
Deustchen Leuten im Süd-Ost-Asien kennenzulernen gelernt haben) erstellt. Die 
Idee ist für dieses App als Online-Game erstellen sodass wir in der Quaräntine 
spielen kann.

Das App hätte die Fähigkeit auf einem Server liegen und dieses Repo wird 
unseren Raum um das App zu entwicklen.

### Bedarf

-   Eine Linux-Schnittstelle
-   Docker oder am mindenstens einem Docker Konto
-   Ein Framework (müssen darauf diskutieren ob wir Nodejs, Apache, Nginx, PHP, etc. verwerden werden)


### Anleitung

### Hinweis

-   Fangen wir mit einem Barebones-App (nur ein Spiel-Session für uns) an