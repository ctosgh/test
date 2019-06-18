import os
import pickle

def store_data():
    jacky = {"name":"jsun", "age":"19", "pay":"100"}
    jacky1 = {"name":"jsun1", "age":"20", "pay":"200"}

    db = {}
    db['jacky'] = jacky
    db['jacky1'] = jacky1

    dbfile = open("db.file", "ab")
    pickle.dump(db, dbfile)
    dbfile.close()

def load_data():
    dbfile = open("db.file", "rb")
    db = pickle.load(dbfile)
    for key in db:
        print("{}===>{}".format(key, db[key]["name"]))

if __name__ == "__main__":
    store_data()
    load_data()
