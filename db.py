import pymongo
import dns


client = pymongo.MongoClient("mongodb+srv://HP:poorna@cluster0.u9cap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['test']
col = db['test1']
# print(db.list_collection_names())
dick = {        "id": 1,
        "starting_time": "16:00",
        "team_a": "Random Team 1",
        "score": "0 - 0",
        "team_b": "Random Team 2",
        "minute": "00:00",
    }

list = [{        "id": 3,
        "starting_time": "136:00",
        "team_a": "Random Te33am 1",
        "score": "0 - 03",
        "team_b": "Rando333m Team 2",
        "minute": "00:020",
    },
    {
        "id": 2,
        "starting_time": "18:00",
        "team_a": "Random Team 3",
        "score": "0 - 0",
        "team_b": "Random Team 4",
        "minute": "00:00",
    }]

# x = col.insert_one(dick)
x = col.insert_many(list)
print(x)
