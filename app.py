from flask import Flask, render_template , request,  redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename

import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///perserta.db'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

#Model
class Peserta(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nama = db.Column(db.String(50))
  alamat = db.Column(db.String(50))
  gender = db.Column(db.String(10))
  umur = db.Column(db.Integer())
  photo = db.Column(db.String(100))
  
  

  def __repr__(self):
    return self.nama
  



@app.route("/list_pendaftaran")
def semua_pendaftaran():
    list_peserta = Peserta.query.all()
    return render_template("list_pendaftaran.html",  tgl = "Tabel Peserta", lp=list_peserta)
     



