from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
def read_root() :
    obj = {
        "message": "안녕하세요!",
        "user" : "YJS"
    }
    return obj

@app.get("/hello")
def hello1(name="hong gildong", password="password") :
    print("[POST] name is", name, "password:", password)
    return {
        "name" : name,
        "password" : password
    }
    
@app.post("/hello")
def hello2(name:str=Form(...), password:str=Form(...)) :
    print("[POST] name is", name, "password:", password)
    return {
        "name" : name,
        "password" : password
    }


