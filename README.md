# Schmeissen

__READ THE [CONTRIBUTING](docs/CONTRIBUTING.md) DOC.__

Schmeißen, Ziehen, Liegen is a german card game that we picked up from our 
german friends during our time in Southeast Asia. Ever since, we've played 
nearly every time that we've met up.

Since the emergence of the COVID-19 pandemic, we've lost the ability to get 
together, thus the inception of this project.

### Documentation

-   [Table of Contents](docs/)
    -   [Contributing](docs/CONTRIBUTING.md)
    -   [Testing](docs/TESTING.md)

### Codebase

#### Technologies

-   ```Flask``` web framework
-   ```Flask-SocketIO``` websockets for bi-directional data flow
-   ```Flask-SQLAlchemy``` ORM
-   ```gunicorn``` WSGI
-   ```SQLite``` development database
-   ```MySQL``` production database

#### Directory Structure

```sh
schmeissen/
├── app         # Core backend
├── docs        # Documentation
├── migrations  # Database migrations
└── src         # Frontend
```

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