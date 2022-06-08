import base64

with open("1.jpg", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
    tt = base64.b64decode(b64_string)
    print(tt)