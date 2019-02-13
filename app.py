import os
import ptvsd
from flask import Flask

DEBUGGER_PORT = os.environ['DEBUGGER_PORT']

try:
    ptvsd.enable_attach(address=('0.0.0.0', DEBUGGER_PORT), secret=None)
    ptvsd.wait_for_attach()
except Exception as ex:
    print('Not working: ')


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
