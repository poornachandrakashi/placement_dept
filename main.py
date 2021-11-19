from flask import Flask, json,request,redirect,url_for
from flask import render_template,jsonify
import csv
import pandas as pd
import requests
import os
from os.path import join, dirname, realpath
from email.message import EmailMessage
import smtplib
EMAIL_ADDRESS = "anonymousoxfordian@gmail.com"
EMAIL_PASSWORD = "poorna1999"

# client = pymongo.MongoClient("mongodb+srv://HP:poorna@cluster0.u9cap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client['test']
# col = db['test1']
# print(db.list_collection_names())


app = Flask(__name__)


contacts = pd.read_csv("static/files/mail.csv")
mails = contacts['Emails'].values


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


@app.route('/write_mail')
def justmail():
     # Set The upload HTML template '\templates\index.html'
    return render_template('mail.html')


@app.route("/write_mail",methods =["GET", "POST"])
def write_mail():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        mail_subject = request.form.get("mail")
        bulk = request.files['file']
        if bulk.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], bulk.filename)
          # set the file path
            bulk.save(file_path)
       # getting input with name = lname in HTML form 
            # content = request.form.get("lname")
        content = request.files['files']
        if content.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], content.filename)
          # set the file path
            content.save(file_path) 

        return redirect(url_for('index'))

@app.route('/mail')
def mails_shoot():
    msg = EmailMessage()
    msg['Subject'] = "TESTING"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ",".join(mails)

    with open("static/files/test.txt") as fp:
    # Create a text/plain message
        msg.set_content(fp.read())
        # msg.set_content('This is a plain text email')

    # msg.add_alternative("""\
    # <!DOCTYPE html>
    # <html>
    # <body>
    #     <h1 style="color:SlateGray;">This is an HTML Emai</h1>
    # </body>
    # </html>
    # """, subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return "Mail Sent"


if __name__ == "__main__":
    app.run(debug=True)