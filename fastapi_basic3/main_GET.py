from fastapi import *
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# public 폴더를 정적 파일 경로로 등록
app.mount("/public", StaticFiles(directory="public", html=True), name="public")

@app.get("/")
def root() :
    return {"message": "Hello! FastAPI"}

# addition(+), subtraction(-), multiplication(*), division(/)

@app.get("/calc/{oper}/{a}/{b}")
def calc(oper: str, a: int, b: int) :
    if oper == "add":
        print (f"덧셈 결과: {a} + {b} = {a+b}")
        return a + b
    elif oper == "sub" :
        print (f"뺄셈 결과: {a} - {b} = {a-b}")
        return a - b
    elif oper == "mul" :
        print (f"곱셈 결과: {a} * {b} = {a*b}")
        return a * b
    elif oper == "div" :
        if b == 0 :
            return "Error(0으로 나눌 수 없음)"
        else :
            print (f"나눗셈 결과: {a} / {b} = {a/b}")
            return round(a/b, 3) 
