## API REST - TO DO w/ login (Olivero - Irastorza)

## Setup del proyecto
- Correr docker compose
```bash
    docker network create db_backend (Si da problemas a la hora de levantar la db)
    docker compose up -d --build
    docker compose logs -f
```
## En caso de tener problemas con composer y querer correrlo local realizar los siguientes comandos
- Instalar dependencias (Composer ya lo realiza)
```bash
    pip install requirements.txt
```
- Inicializar xampp y crear base de datos 'todo'.
- Correr las migraciones en flask a partir de los siguientes comandos (borrar carpeta migraciones si ya hay una existente, al no estar dockerizado, puede existir un error al correr las mismas):
```python
    flask db init
    flask db migrate -m 'Initial migration'
    flask db upgrade
```
## Login 
```sql
    - Metodo: GET
    - Endpoint: 127.0.0.1/login 
```

# Importante
##### Para hacer uso de los endpoints de admin, es necesario logearse y obtener el x-access-token que nos brinda la API, a traves del mismo se corroborara si un usuario es admin o no, este valor es necesario que se coloque en los headers a la hora de realizar una peticion.

## Endpoints disponibles admin
#### Obtener todos los usuarios: 
```sql
    - Metodo: GET
    - Endpoint: 127.0.0.1/user
```

#### Obtener un usuario: 
```sql
    - Metodo: GET
    - URL Parameter: public_id
    - Endpoint: 127.0.0.1/user/<public_id>
```

#### Crear un usuario: 
```sql
    - Metodo: POST
    - Ejemplo body: { "name": "Quiricocho", "password": "1234" }
    - Ejemplo: 127.0.0.1/user
```

#### Hacer admin a un usuario (cambia el booleano de la base de datos, y le otorga permisos de admin): 
```sql
    - Metodo: PUT
    - URL Parameter: public_id
    - Ejemplo: 127.0.0.1/user/<public_id>
```

#### Borrar usuario: 
```sql
    - Metodo: DELETE
    - URL Parameter: public_id
    - Ejemplo: 127.0.0.1/user/<public_id>
```

## Endpoints disponibles to do app
#### Obtener todas las tareas (segun usuario, el cual ya lo obtiene por la autentificacion): 
```sql
    - Metodo: GET
    - Endpoint: 127.0.0.1/todo
```

#### Obtener una tarea: 
```sql
    - Metodo: GET
    - URL Parameter: todo_id
    - Endpoint: 127.0.0.1/todo/<todo_id>
```

#### Crear una tarea: 
```sql
    - Metodo: POST
    - Ejemplo body: { "text": "Lavar los platos" }
    - Ejemplo: 127.0.0.1/todo
```

#### Marcar tarea como completada: 
```sql
    - Metodo: PUT
    - URL Parameter: todo_id
    - Ejemplo: 127.0.0.1/todo/<todo_id>
```

#### Borrar tarea: 
```sql
    - Metodo: DELETE
    - URL Parameter: todo_id
    - Ejemplo: 127.0.0.1/todo/<todo_id>
```


