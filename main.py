from flask import Flask, json,request,redirect,url_for
from flask import render_template,jsonify
import csv
import pandas as pd
import pymongo
import dns
import requests
import os
from os.path import join, dirname, realpath

# client = pymongo.MongoClient("mongodb+srv://HP:poorna@cluster0.u9cap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client['test']
# col = db['test1']
# print(db.list_collection_names())


app = Flask(__name__)





@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/ise')
# def ise():
#     dummy_data = data_json()
#     return render_template('ise.html',matches = dummy_data.json)

@app.route('/ise')
def ise_main():
    data=pd.read_csv('static/files/ise.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('ISE.html',results=result)
    


@app.route('/cs')
def cs_main():
    data=pd.read_csv('cse.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('cse.html',results=result)


# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


# Root URL
@app.route('/upload')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('upload.html')


# Get the uploaded files
@app.route("/upload", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
          # save the file
      return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)