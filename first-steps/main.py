from fastapi import FastAPI

# Inicializamos
app = FastAPI(title='Mini Blog')


# Creamos una constante 
BLOG_POST = [
    {'id':1, 'title': 'Hola desde FastAPI', 'Content': 'Mi primer post con FastAPI'},
    {'id':2, 'title': 'Hola desde FastAPI', 'Content': 'Mi segundo post con FastAPI'},
    {'id':3, 'title': 'Hola desde FastAPI', 'Content': 'Mi tercer post con FastAPI'}
]

@app.get('/')
def home():
    return {"message": 'Bienvenidos a mi Mini Blog'}


@app.get('/posts')
def list_posts():
    return {'data': BLOG_POST}