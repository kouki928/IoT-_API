import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from ..main import parkingData

# Use a service account.
cred = credentials.Certificate('firebase_config/iotsocialapp-firebase-adminsdk-h6izh-0af48e1137.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

def GetAllDoc(docName):
    users_ref = db.collection(docName)
    docs = users_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
        
def insertParkingData(pk_data: parkingData):
    parkingId = pk_data.parkingId
    data = {"percent": pk_data.percent}
    db.collection("Parking").document(parkingId).update(data)
        
        
# def insertParkingData(pk_data):
#     deviceId = pk_data.deviceId
#     percent  = pk_data.percent
#     db.collection("Parking").document(deviceId).update({
#         "percent" : percent
#     })