# Si quiero hacer algun tipo de filtrado, buscar o personalizar una respuesta, usaremos los Query Params

from fastapi import FastAPI
from fastapi import Query

# Inicializamos
app = FastAPI(title='Mini Blog')


# Creamos nuestra fuente de datos (usualmente es una BD, pero esto basta para nuestros primeros pasos)
BLOG_POST = [
    {'id':1, 'title': 'Hola desde FastAPI', 'Content': 'Mi primer post con FastAPI'},
    {'id':2, 'title': 'Hoy hay nuevo campeon del mundo', 'Content': 'Mi segundo post con FastAPI'},
    {'id':3, 'title': 'EL fin de la era de Messi', 'Content': 'Mi tercer post con FastAPI'}
]

@app.get('/')
def home():
    return {"message": 'Bienvenidos a mi Mini Blog'}


@app.get('/posts')
def list_posts(query: str | None = Query(default=None, description='Texto para buscar por titulo')):
    '''
    Metodo GET para obtener los datos filtrados con una Query
    '''

    if query:
        resultados = [post for post in BLOG_POST if query.lower() in post['title'].lower()] 
        return {'data': resultados, 'query': query}

    else:
        return {'data': BLOG_POST}