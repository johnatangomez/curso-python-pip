import store
from fastapi import FastAPI # type: ignore
from fastapi.responses import HTMLResponse # type: ignore

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1> Hola soy una pagina</h1>
        <p> Soy un parrafo </p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()