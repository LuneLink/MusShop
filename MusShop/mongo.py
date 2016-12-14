import json

from pymongo import MongoClient


class Mongo:
    client = MongoClient()
    db = client['mydb']

    def getInstrumentsByType(self, type):
        print "TYPE"
        print type
        # dict = self.db.instruments.find({"type": type})
        dict = self.db.instruments.find({"type": long(type)}, {'_id': False})

        mylist = []
        for document in dict:
            mylist.append(document)
            print document

        return mylist

    def getInstrumentByModel(self, model):
        dict = self.db.instruments.find({"model": model}, {'_id': False})

        mylist = []
        for document in dict:
            mylist.append(document)
            print document

        return mylist

    def getInstrumentByManufacturer(self, name):
        dict = self.db.instruments.find({"manufacturer__name": name}, {'_id': False})

        mylist = []
        for document in dict:
            mylist.append(document)
            print document

        return mylist

    def getInstrumentByCost(self, cost):
        dict = self.db.instruments.find({"coast": long(cost)}, {'_id': False})

        mylist = []
        for document in dict:
            mylist.append(document)
            print document

        return mylist

    def getInstrumentById(self, id):
        dict = self.db.instruments.find({"id": long(id)}, {'_id': False})

        mylist = []
        for document in dict:
            mylist.append(document)
            print document

        return mylist

    def updateInstrument(self, id, newCount):
        self.db.instruments.update({'id': id}, {'count': newCount})

    def getSizes(self):
        return self.db.sizes.find()

    def getManufacturers(self):
        return self.db.manufacturers.find()

    def getType(self, id):
        return self.db.types.find()

    def insertInstrument(self):
        # self.db.instruments.insert({"wat": "wat?"})
        # for d in doc:
        #     print d
        #     self.db.instruments.insert(d)
        print "insert"
        self.db.instruments.insert({'model': u'KingV', 'type': 1L, 'id': 1L,
                                    'manufacturer__name': u'Jackson', 'coast': 100L}, {'autoIndexId': False})
        self.db.instruments.insert({'model': u'Minion', 'type': 1L, 'id': 2L,
                                    'manufacturer__name': u'Jackson', 'coast': 200L}, {'autoIndexId': False})
        print "inserted"

    def create(self):
        print "Start creation"

        print "1"
        print "2"
        post = {"author": "Mike",
                "text": "My first blog post!",
                "tags": ["mongodb", "python", "pymongo"]}
        print "3"
        # post_id = self.db.user_actions.insert(post)

        # print "POST ID"
        # print post_id

        cursor = self.db.user_actions.find()
        for document in cursor:
            print document

        print "Created"
        return True