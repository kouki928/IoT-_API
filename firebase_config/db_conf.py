import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('firebase_config/iotsocialapp-firebase-adminsdk-h6izh-0af48e1137.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

def GetAllDoc(docName):
    users_ref = db.collection(docName)
    docs = users_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")