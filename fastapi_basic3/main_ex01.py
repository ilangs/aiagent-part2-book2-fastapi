from fastapi import *
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# get 메서드를 postman으로 테스트 
@app.get("/")
def root(message: str, age: int) :
    return {
        "message": message,
        "message length" : len(message),
        "age" : age
    }


# post 메서드를 추가하고 postman으로 테스트 
@app.post("/")
def root(message: str, age: int) :
    return {
        "message": message,
        "message length" : len(message),
        "age" : age
    }


# Form 파라미터 전달받아 postman으로 테스트 
@app.post("/login")
def login_post(username: str = Form(...)) :
    return {
        "username": username
    }


# Basemodel을 상속받아서 Message 클래스 선언
# (postman) Content-Type: raw로 설정 후 JSON data 설정
from pydantic import BaseModel

class Message(BaseModel) :
    text: str 

@app.post("/login")
def root(message:Message) :
    print("Post - 요청 받았다.")
    return {
        "message" : message.text
    }


# Ajax 활용, public 폴더를 정적 파일 경로로 등록
app.mount("/public", StaticFiles(directory="public", html=True), name="public")

