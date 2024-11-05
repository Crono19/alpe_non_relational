from mongoengine import Document, StringField, ListField, EmbeddedDocument, EmbeddedDocumentField

# Define an embedded document for phone numbers
class PhoneNumber(EmbeddedDocument):
    number = StringField(required=True)

# Define the main document for clients
class Client(Document):
    meta = {'collection': 'clients'}  # Specify the collection name

    code = StringField(required=True)
    nit = StringField(required=True)
    name = StringField(required=True)
    direction = StringField()
    phone_numbers = ListField(EmbeddedDocumentField(PhoneNumber))
