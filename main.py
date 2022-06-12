from fastapi import FastAPI, File, UploadFile #import class FastAPI() từ thư viện fastapi
import requests
app = FastAPI() # gọi constructor và gán vào biến app

@app.get("/") # giống flask, khai báo phương thức get và url
async def root(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return {"message": "Xin chào đây là đội Xanh nước biển"}




@app.post('/img') # Post gửi ảnh CMND để trích xuất thông tin
async def create_file(file: bytes = File()):
    url = 'https://api.fpt.ai/vision/idr/vnm'
    files = {'image': file}
    headers = {
        'api-key': 'krhqw0LvJpuS0hRtYYlW1yy8yZjdMaps'
    }
    response = requests.post(url, files=files, headers=headers).json()

    try:
        data = {
            'code' : response['data'][0]['id'],
            'fullname' : response['data'][0]['name'],
            'birthday' : response['data'][0]['dob'],
            'gender' : response['data'][0]['sex'],
            'nation' : response['data'][0]['ethnicity'],
            'location' : response['data'][0]['home'],
            'address' : response['data'][0]['address']
        }
    except:
        data = {
        'code' : response['data'][0]['id'],
        'fullname' : response['data'][0]['name'],
        'birthday' : response['data'][0]['dob'],
        'gender' : response['data'][0]['sex'],
        'nation' : ' ',
        'location' : response['data'][0]['home'],
        'address' : response['data'][0]['address']
    }
    return data



