from fastapi import FastAPI


app = FastAPI()

data = "Hello World!"


@app.get("/")
def index() -> set[str]:
    return{"data", data}