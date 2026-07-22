Para probar el endpoint de la clase 48, aunque lo podemos hacer con FastAPI directamente, lo vamos a porbar con postman y con Curl.

### Probando con Curl

```bash
curl -X POST http://127.0.0.1:8000/post \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Nuevo post desde Curl",
    "content": "Mi nuevo post desde Curl (terminal)"
  }'
```

Esta petición envía datos a una API local para crear un recurso nuevo, en este caso un post.

- `curl`: herramienta de línea de comandos que permite realizar peticiones HTTP.
- `-X POST`: define que se usará el método HTTP `POST`, normalmente destinado a crear nuevos recursos.
- `http://127.0.0.1:8000/post`: URL del endpoint de la API.
  - `127.0.0.1` representa la computadora local.
  - `8000` es el puerto donde se está ejecutando el servidor.
  - `/post` es la ruta que recibe la petición.
- `-H "Content-Type: application/json"`: agrega un encabezado HTTP (*header*) que indica que el cuerpo de la petición está escrito en formato JSON.
- `-d`: especifica los datos que se enviarán en el cuerpo (*body*) de la petición.
- `title` y `content`: campos del objeto JSON enviados al endpoint.

La respuesta que se arroja despues de la peticion es esta:

```json
{"message":"Post creado","data":{"id":4,"title":"Nuevo post desde Curl","content":"Mi nuevo post desde Curl (terminal)"}}
```