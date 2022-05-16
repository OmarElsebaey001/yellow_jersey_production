from flask import Flask
from operator import methodcaller
from flask import make_response,Flask,render_template
from flask import request, jsonify
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from helper import convert_and_append 
from jinja2 import Template
from flask import send_file
from helper import create_image 
import io 
from random import randint
import threading
import time

mutex = threading.Lock()  # is equal to threading.Semaphore(1)


img = Image.open("l.jpeg").convert('RGB')
app = Flask(__name__)

@app.route("/",methods=['GET'])
def show():
    capital        = request.args.get('cl_nt_cp', default = 1, type = float)
    total          = request.args.get('cl_tot_po', default = 1, type = float)
    sub_name       = request.args.get('cl_nm', default = 1, type = str)
    wealth_manager = request.args.get('wlt_mng', default = 1, type = str)
    wealth_number  = request.args.get('wlt_mng_nm', default = 1, type = str)
    date           = request.args.get('date', default = 1, type = str)

    wlt_mang_num   = f"+{wealth_number[0:2]} {wealth_number[2:7]} {wealth_number[7:]}"
    wealth_manager = wealth_manager + f": {wlt_mang_num}"
    capital = int(capital)
    total = int(total)
    with mutex :
        print("MUTEX GAINED")
        forg_img,back_img = create_image(capital,total,sub_name,wealth_manager,date,img)
    full_pic = convert_and_append(forg_img,back_img)
    buf = io.BytesIO()
    full_pic.save(buf, "JPEG", quality=100, optimize=True, progressive=True)
    buf.seek(0)
    return send_file(buf,mimetype='image/jpeg')

@app.route("/hi")
def hi():
        return "New Hello"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
