import os
import ptvsd
from flask import Flask

DEBUGGER_PORT = int(os.environ['DEBUGGER_PORT'])

try:
    print('Starting debugger...')
    ptvsd.enable_attach(address=('0.0.0.0', DEBUGGER_PORT), secret=None)
    print('Waiting for attach...')
    ptvsd.wait_for_attach()
except Exception as ex:
    print('Debugger setup failed: ')
    raise ex


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
