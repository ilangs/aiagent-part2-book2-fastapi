# 실습 : 
# 1. join-us.html 파일을 만든다
# 2. 신상 정보 입력 받을 수 있도록 form 구현
# 3. 성명, 주소, 전화번호, email, 나이, 성별 등
# 4. main.py에서 데이터를 전송 받아다서 터미널에 출력 or 파일 저장

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 1. 메인 페이지 (폼 불러오기)
@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse("join-us.html", {"request": request})

# 2. 폼에서 데이터 전송 후 처리
@app.post("/join")
def join_submit(
    name: str = Form(...),
    address: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...)
):
    
    print(">>>> [POST - /join]", name, address, phone, email, age, gender)

