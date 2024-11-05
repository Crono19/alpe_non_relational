# webapp/models.py
from mongoengine import Document, StringField, ListField, EmbeddedDocument, EmbeddedDocumentField

class PhoneNumber(EmbeddedDocument):
    number = StringField(required=True, db_field="Number")  # Match the MongoDB field name

class Client(Document):
    meta = {'collection': 'clients'}  # Specify the collection name

    code = StringField(required=True, db_field="Code")        # Match the MongoDB field name
    nit = StringField(required=True, db_field="NIT")
    name = StringField(required=True, db_field="Name")
    direction = StringField(db_field="Direction")
    phone_numbers = ListField(EmbeddedDocumentField(PhoneNumber), db_field="PhoneNumbers")

