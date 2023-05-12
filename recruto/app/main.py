from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
async def hello(request: Request, name: str = "Rekruto", message: str = "Давай дружить!"):
    nl = '\n'
    # Формируем сообщение и выводим его на странице
    return f'Hello {name}! {nl} {message}!'

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")
