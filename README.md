## EFI Python - Irastorza - Olivero

## API REST - TO DO w/ login
https://vip2picallex.atlassian.net/browse/ITDR-266

## Setup del proyecto

- Inicializar xampp y crear base de datos 'todo'.
- Correr las migraciones en flask a partir de los siguientes comandos:
```python
    flask db init
    flask db migrate -m 'Initial migration'
    flask db upgrade
```

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
    - Endpoint: 127.0.0.1/user/737
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
    - Ejemplo: 127.0.0.1/user/737
```

#### Borrar usuario: 
```sql
    - Metodo: DELETE
    - URL Parameter: public_id
    - Ejemplo: 127.0.0.1/user/737
```

## Endpoints disponibles to do app
#### Obtener todas las tareas (segun usuario, el cual ya lo obtiene por la autentificacion): 
```sql
    - Metodo: GET
    - Endpoint: 127.0.0.1/todo
```

#### Obtener un usuario: 
```sql
    - Metodo: GET
    - URL Parameter: public_id
    - Endpoint: 127.0.0.1/user/737
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
    - Ejemplo: 127.0.0.1/user/737
```

#### Borrar usuario: 
```sql
    - Metodo: DELETE
    - URL Parameter: public_id
    - Ejemplo: 127.0.0.1/user/737
```


