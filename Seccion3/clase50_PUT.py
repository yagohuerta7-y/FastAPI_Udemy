from fastapi import FastAPI
from fastapi import Query
from fastapi import Body
from fastapi import HTTPException

# Inicializamos
app = FastAPI(title='Mini Blog')


# Creamos nuestra fuente de datos (usualmente es una BD, pero esto basta para nuestros primeros pasos)
BLOG_POST = [
    {'id':1, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post con FastAPI'},
    {'id':2, 'title': 'Hoy hay nuevo campeon del mundo', 'content': 'Mi segundo post con FastAPI'},
    {'id':3, 'title': 'EL fin de la era de Messi', 'content': 'Mi tercer post con FastAPI'}
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


@app.get('/post/{post_id}')
def get_post(post_id: int, query: int | None = Query(default=1, description='0 si no quieres el contenido, 1 si lo quieres')):
    '''
    Metodo GET para obtener un post especifico a partir del 'id'
    '''

    if query==1:
        for post in BLOG_POST:
            if post['id'] == post_id:
                return {'data': post}
            
            else:
                return {'Error': 'Post no encontrado'}
            
    elif query==0:
        claves = ['id', 'title']

        for post in BLOG_POST:
            if post['id'] == post_id:
                seleccion = {clave: post[clave] for clave in claves}
                return {'data': seleccion}

            else:
                return {'Error': 'Post no encontrado'}


@app.post('/post')
def create_post(post: dict = Body(...)): # Agregamos los tres puntos para que sea obligatorio
    '''
    Metodo POST para agrgar un nuevo post
    '''

    if 'title' not in post or 'content' not in post:
        return {'Error': 'Title y Content son requeridos'}
    
    if not str(post['title']).strip():
        return {'Error': 'Title no puede estar vacio'}
    
    new_id = (BLOG_POST[-1]['id'] + 1) if BLOG_POST else 1

    new_post = {'id': new_id, 'title': post['title'], 'content': post['content']}

    BLOG_POST.append(new_post)

    return {'message': 'Post creado', 'data': new_post}


@app.put('/posts/{post_id}')
def update_post(post_id: int, data: dict = Body(...)):
    '''
    Metodo PUT para actualizar un post
    '''

    # Recorremos los post hasta encontrar el que queremos modificar
    for post in BLOG_POST:
        if post['id'] == post_id:

            if 'title' in data:
                post['title'] = data['title'] # Actualizamos el title del post con el nuevo

            if 'content' in data:
                post['content'] = data['content'] # Actualizamos el content del post con el nuevo

            return {'message': 'Post actualizado', 'data': post}
        
    raise HTTPException(status_code=404, detail='Post no encontrado')    