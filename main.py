from fastapi import FastAPI, File, UploadFile #import class FastAPI() từ thư viện fastapi
import requests
app = FastAPI() # gọi constructor và gán vào biến app
import json

@app.get("/") # giống flask, khai báo phương thức get và url
async def root(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return {"message": "Hello World 1"}




@app.post('/img') # Post gửi ảnh CMND để trích xuất thông tin
async def create_file(file: bytes = File()):
    url = 'https://api.fpt.ai/vision/idr/vnm'
    files = {'image': file}
    headers = {
        'api-key': '7CMshx6GwrGPG5gfen9DJ8wnGuHjQpJa'
    }
    response = requests.post(url, files=files, headers=headers).json()

    
    data = {
        'so_cmnd' : response['data'][0]['id'],
        'ho_ten' : response['data'][0]['name'],
        'sinh_nhat' : response['data'][0]['dob'],
        'gioi_tinh' : response['data'][0]['sex'],
        'dan_toc' : response['data'][0]['ethnicity'],
        'que_quan' : response['data'][0]['home'],
        'thuong_tru' : response['data'][0]['address'],
        'han_su_dung' : response['data'][0]['doe']
    }
    return data
