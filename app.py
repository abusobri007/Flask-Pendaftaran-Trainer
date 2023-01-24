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
  




@app.route('/tambah_peserta/')
def semua_pendaftar():
    return  render_template("tambah_peserta.html")

@app.route("/tambah_peserta/save", methods=['POST'])
def save_peserta():
    if request.method == 'POST':
        #membuat objek peserta
       f_nama =request.form.get("nama")
       f_alamat =request.form.get("alamat")
       f_gender =request.form.get("gender")
       f_umur =request.form.get("umur")
       
       p = Peserta(nama=f_nama, alamat=f_alamat,gender=f_gender, umur=f_umur, photo=f_photo)
       
       db.session.add(p)
       db.session.commit()
       return redirect('/list_pendaftaran')
    return redirect('/tambah_peserta')


if "__main__" ==__name__:
     app.run(debug= True,port =2000)
