from fastapi import *
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# Ajax 활용, public 폴더를 정적 파일 경로로 등록
app.mount("/public", StaticFiles(directory="public", html=True), name="public")


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
    return {
        "message" : message.text
    }


