# 실습 : 
# 1. join-us.html 파일을 만든다
# 2. 신상 정보 입력 받을 수 있도록 form 구현
# 3. 성명, 주소, 전화번호, email, 나이, 성별 등
# 4. main.py에서 데이터를 전송 받아다서 터미널에 출력 or 파일 저장

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import csv
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 1. 메인 페이지 (폼 불러오기)
@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse("join-us.html", {"request": request})

# 2. 폼에서 데이터 전송 후 처리
@app.post("/join")
def join_submit(
    request: Request,  # 템플릿 사용을 위해 request 인자 필요
    name: str = Form(...),
    address: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...)
):
    
    # print(">>>> [POST - /join]", name, address, phone, email, age, gender)
    
    user_info = {
        "성명": name,
        "주소": address,
        "전화": phone,
        "이메일": email,
        "나이": age,
        "성별": gender
    }

    # 터미널에 출력
    print("\n[회원가입 정보]")
    for k, v in user_info.items():
        print(f"{k}: {v}")

    # # csv 파일로 저장 (append)
    # CSV_FILE = "user_info.csv"
    # with open(CSV_FILE, "a+", newline="", encoding="utf-8") as f:
    #     writer = csv.writer(f)
        
    #     # 파일이 비어 있을 때만 헤더 한번만 작성
    #     f.seek(0)
    #     first_line = f.readline().strip()
    #     if not first_line :
    #         writer.writerow(["submitted_at", "name", "address", "phone", "email", "age", "gender"])
    #     # 실제 데이터 한 줄 추가
        
    #     writer.writerow([
    #         datetime.now().strftime("%Y-%m-%d"), name, address, phone, email, age, gender
    #     ])
 
    return templates.TemplateResponse("result.html", {"request": request, **user_info})

    # return HTMLResponse(f"""
    #     <!DOCTYPE html>
    #     <html lang="ko">
    #         <head>
    #             <meta charset="UTF-8">
    #             <title>결과 페이지</title>
    #         </head>
    #         <body>
    #             <ul>
    #                 <li><strong>성명: {name}</li>
    #                 <li><strong>주소: {address}</li>
    #                 <li><strong>전화: {phone}</li>
    #                 <li><strong>Email {email}</li>
    #                 <li><strong>나이: {age}</li>
    #                 <li><strong>성별: {gender}</li>
    #             </ul>
    #             <hr>
    #             <a href="/">홈으로 돌아가기</a>
    #         </body>
    #     </html>               
    # """)
