from flask import Flask, json
from flask import render_template,jsonify
import pymongo
import dns

client = pymongo.MongoClient("mongodb+srv://HP:poorna@cluster0.u9cap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['test']
col = db['test1']
# print(db.list_collection_names())


app = Flask(__name__)

@app.route('/data_json')
def data_json():
    dummy_data = [
    {
        "id": 1,
        "Name": "Poornachandra H Kashi",
        "Branch": "ISE",
        "Company": "Brillio",
        "Package": "4.5+4 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 2,
        "Name": "Akhel P",
        "Branch": "ISE",
        "Company": "Brillio",
        "Package": "4.5+4 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 3,
        "Name": "Dhanush N S",
        "Branch": "ISE",
        "Company": "Brillio",
        "Package": "4.5+4 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 4,
        "Name": "Pankaj R Gurav",
        "Branch": "ISE",
        "Company": "Cognizent",
        "Package": "4 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 5,
        "Name": "Navya.T",
        "Branch": "ISE",
        "Company": "Cognizent",
        "Package": "4 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 6,
        "Name": "Neha R",
        "Branch": "ISE",
        "Company": "Cognizent",
        "Package": "4 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 7,
        "Name": "Ayesha Rahman Aiman",
        "Branch": "ISE",
        "Company": "Cognizent",
        "Package": "4 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 8,
        "Name": "Aishwarya N",
        "Branch": "ISE",
        "Company": "Cognizent",
        "Package": "4 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 9,
        "Name": "Jyothi G",
        "Branch": "ISE",
        "Company": "Cognizent",
        "Package": "4 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 10,
        "Name": "Inchara T",
        "Branch": "ISE",
        "Company": "Cognizent",
        "Package": "7 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 11,
        "Name": "Jyothi G",
        "Branch": "ISE",
        "Company": "Cognizent",
        "Package": "4 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 12,
        "Name": "Ishita soni",
        "Branch": "ISE",
        "Company": "Atos Syntel",
        "Package": "3.1 LPA",
        "Passing_Year": "2022",
    },
        {
        "id": 13,
        "Name": "Rutu Patel",
        "Branch": "ISE",
        "Company": "Atos Syntel",
        "Package": "3.1 LPA",
        "Passing_Year": "2022",
    },
        {
        "id": 14,
        "Name": "Megha Mathew",
        "Branch": "ISE",
        "Company": "Atos Syntel",
        "Package": "3.1 LPA",
        "Passing_Year": "2022",
    },
        {
        "id": 15,
        "Name": "Arpita Nanda",
        "Branch": "ISE",
        "Company": "Atos Syntel",
        "Package": "3.1 LPA",
        "Passing_Year": "2022",
    },
    {
        "id": 16,
        "Name": "Aradhana M K",
        "Branch": "ISE",
        "Company": "Atos Syntel",
        "Package": "3.1 LPA",
        "Passing_Year": "2022",
    }
    ]
    return jsonify(dummy_data)


# @app.route('/data')
# def read():
#     documents = db.test.find()
#     response = []
#     for document in documents:
#         document['_id'] = str(document['_id'])
#         response.append(document)
#     return json.dumps(response)

@app.route('/')
def home():
    return "Hello World"

@app.route('/ise')
def ise():
    dummy_data = data_json()
    return render_template('index.html',matches = dummy_data.json)




if __name__ == "__main__":
    app.run(debug=True)