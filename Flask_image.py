# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:12:32 2020

@author: Abhimanyu
"""

from flask import request, redirect, Flask, render_template
from process_image import process_img
import os
import numpy as np
import base64
from io import BytesIO
from PIL import Image
import re
import io
app = Flask(__name__)


@app.route("/digit-classifier", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":
        #print(request.form)

        if request.form:

            image_b64 = request.form["img"]
            content = image_b64.split(';')[1]
            data = content.split(',')[1]
            body = base64.decodebytes(data.encode('utf-8'))
            #print(body)
            image = Image.open(io.BytesIO(body))
            image.save('upload.jpg')
            #image.save(os.path.join('upload'))
            k = process_img()
            return str(k)

            #return "The number is "+str(k)


    return render_template("upload_image.html")


@app.route("/lol", methods=["GET", "POST"])
def up():
    return render_template("upload_image.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)