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
  
@app.route("/list_pendaftaran/<id>/delete")
def delete_pendafar(id):
    obj = Peserta.query.filter_by(id=id).first()
    db.session.delete(obj)
    db.session.commit()
    return redirect('/list_pendaftaran')





    return render_template("load_image.html")
if "__main__" ==__name__:
     app.run(debug= True,port =2000)
