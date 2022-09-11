
# REST API CRUD - POLITECNICO

Esta REST API simula el registro de un periodo escolar en un politecnico. 

Permitiendo crear profesores, aulas, alumnos y asignar a los alumnos a sus respectivas aulas
y por tanto a los maestros el turno en el cual impartiran sus clases.


## Screenshots

![Screenshot_10](https://user-images.githubusercontent.com/60016712/189532679-ae3dde84-6ec4-4d5b-b814-6f3f0fd1edff.png)


## Documento tecnicos
![Diagrama ER de base de datos (POLITECNICO) (1)](https://user-images.githubusercontent.com/60016712/189537513-0882db51-9d06-484a-9982-bfb91b622f8c.jpeg)
## How to run


```bash
  git clone https://github.com/No-Hex/RestApi_Politecnico.git

  cd RestApi_Politecnico
```

```bash
  cd backend

  pip install -r requirements.txt
```
## Variables de entorno

Crear un archivo .env y añadir las siguientes variables con la informacion
requerida.

```bash
SECRETKEY=''

DATABASE_NAME=''
DATABASE_USER=''
DATABASE_PASS=''
DATABASE_HOST=''
DATABASE_PORT=''
```
Migraciones
```bash
  py manage.py makemigrations

  py manage.py migrate
```
## Run server.
```bash
  py manage.py runserver
```
## Tech Stack

**Framework:** Django, Django REST framework

**Language:** Python

**Database:** PostgreSQL

