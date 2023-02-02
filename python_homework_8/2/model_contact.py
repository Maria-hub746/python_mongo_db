from mongoengine import Document, connect
from mongoengine.fields import StringField, EmailField, BooleanField



class Contacts(Document):
    name = StringField()
    email = EmailField()
    sending = BooleanField()
    email_priority = BooleanField()