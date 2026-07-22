# Maneras de ejecutar los scripts

Hay dos maneras de ejecutar tus scripts, la primera es con fastapi:

```python
uv run fastapi dev tu_script.py
```

Y la segunda es con uvicorn:

```python
uvicorn main:app --reload
```

Si quieres usar otro puerto (ej. el 9000) solo agrega:

```python
uvicorn main:app --reload --port 9000
```
