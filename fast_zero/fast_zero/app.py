from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', status_code=200)
def read_root():
    return {'message': 'Hello, World!'}


@app.get('/home', status_code=200, response_class=HTMLResponse)
def read_home():
    return """
        <!DOCTYPE html>
            <html lang="en">
            <head>
             <meta charset="UTF-8">
            <meta content="width=device-width,
            initial-scale=1.0">
            <title>Document</title>
            </head>

            <style>
                body {
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                }
            </style>
            <body>
             <h1>Olá Mundo!</h1>
                 <hr>
                 <p>teste em html web</p>
            </body>
            </html>
    """
