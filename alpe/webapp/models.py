from mongoengine import Document, StringField, IntField 

class Client(Document):
    meta = {'collection': 'clients'}
    name = StringField(required=True)
    email = StringField()
