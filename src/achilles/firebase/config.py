import firebase_admin
import os

def configure_firebase_admin():
    if (not len(firebase_admin._apps)):
        abs_file_path = os.environ['FIREBASE_CREDENTIALS']
        cred = firebase_admin.credentials.Certificate(abs_file_path)
        default_app = firebase_admin.initialize_app(cred)
        return default_app
