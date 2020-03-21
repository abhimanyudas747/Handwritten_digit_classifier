# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:12:32 2020

@author: Abhimanyu
"""

from flask import request, redirect, Flask, render_template
from process_image import process_img
import os
app = Flask(__name__)


@app.route("/upload_image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            
            image.save(os.path.join('upload'))
            k = process_img()

            return "The number is "+str(k)


    return render_template("upload_image.html")


@app.route("/lol", methods=["GET", "POST"])
def up():
    return render_template("upload_image.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)