from flask import Flask, render_template , request,  redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename

import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///perserta.db'
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.dirname(__file__)) + "\static\media/"
ALLOWED_EXTENSIONS = { 'pdf', 'png', 'jpg', 'jpeg'}

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
  
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/list_pendaftaran/<id>/edit")
def edit_peserta(id):
    obj = Peserta.query.filter_by(id=id).first()
    return render_template("edit_peserta.html",obj=obj)

@app.route("/list_pendaftaran/<id>/update", methods=['POST'])
def update_peserta(id):
    obj = Peserta.query.filter_by(id=id).first()#data from db
 #data from cline server
    f_nama = request.form.get("nama")
    f_alamat = request.form.get("alamat")
    f_gender = request.form.get("gender")
    f_umur = request.form.get("umur")
    photo = request.files['Photo']
    print(photo.filename)
    
    if photo.filename== '':
           flash("Photo tidak boleh kosong")
    
    if photo and allowed_file(photo.filename):
       filename= secure_filename(photo.filename)

       photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       f_photo = os.path.join('static\media', filename)
    #data form db whiht data from cline server
    obj.nama=f_nama
    obj.alamat=f_alamat
    obj.gender=f_gender
    obj.umur=f_umur
    obj.photo=f_photo

    #save perubahan data ke db

    db.session.add(obj)
    db.session.commit()
    return redirect('/list_pendaftaran')




    
       
    


if "__main__" ==__name__:
     app.run(debug= True,port =2000)
