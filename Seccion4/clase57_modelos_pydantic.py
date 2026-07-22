from fastapi import FastAPI
from fastapi import Query
from fastapi import Body
from fastapi import HTTPException
from pydantic import BaseModel


# Inicializamos
app = FastAPI(title='Mini Blog')


# Creamos nuestra fuente de datos (usualmente es una BD, pero esto basta para nuestros primeros pasos)
BLOG_POST = [
    {'id':1, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post con FastAPI'},
    {'id':2, 'title': 'Hoy hay nuevo campeon del mundo', 'content': 'Mi segundo post con FastAPI'},
    {'id':3, 'title': 'EL fin de la era de Messi', 'content': 'Mi tercer post con FastAPI'}
]


# Definimos los modelos de datos con Pydantic

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: str
    content: str



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
def create_post(post: PostCreate): # Aqui actualizamos el parametro del endpoint, ya no es Body(...), ahora es el esquema de Pydantic
    '''
    Metodo POST para agrgar un nuevo post
    '''

    new_id = (BLOG_POST[-1]['id'] + 1) if BLOG_POST else 1
    new_post = {'id': new_id, 'title': post.title, 'content': post.content}
    BLOG_POST.append(new_post)

    return {'message': 'Post creado', 'data': new_post}


@app.put('/posts/{post_id}')
def update_post(post_id: int, data: PostUpdate):
    '''
    Metodo PUT para actualizar un post
    '''

    # Recorremos los post hasta encontrar el que queremos modificar
    for post in BLOG_POST:
        if post['id'] == post_id:

            playload = data.model_dump(exclude_unset=True) # Transformamos la data (que es objeto) a un diccionario

            if 'title' in playload:
                post['title'] = playload['title'] # Actualizamos el title del post con el nuevo

            if 'content' in playload:
                post['content'] = playload['content'] # Actualizamos el content del post con el nuevo

            return {'message': 'Post actualizado', 'data': post}
        
    raise HTTPException(status_code=404, detail='Post no encontrado')


@app.delete('/posts/{post_id}', status_code=204) # Si todo sale bien, solo retorna el codigo 204
def delete_post(post_id: int):
    '''
    Metodo DELETE para borrar un post
    '''

    for index, post in enumerate(BLOG_POST):
        if post['id'] == post_id:
            BLOG_POST.pop(index)

            return

        raise HTTPException(status_code=404, detail='Post no encontrado')