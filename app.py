from flask import Flask, render_template , request,  redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename

import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///perserta.db'
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.dirname(__file__)) + "\static\media/"
ALLOWED_EXTENSIONS = { 'pdf', 'png', 'jpg', 'jpeg'}


def welcom_To_Itec():
  return{
         "message" : "Welcom to itec mataram"       
  }



if "__main__" ==__name__:
     app.run(debug= True,port =2000)
