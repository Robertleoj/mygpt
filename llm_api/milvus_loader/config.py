from dotenv import load_dotenv
import os

LOADED = False

def initialize():
    global LOADED

    if os.path.exists('.env') and not LOADED:
        load_dotenv()

    LOADED = True
    

def get_config(key, default=None):

    initialize()
    if default is None:
        return os.getenv(key)
    else:
        return os.getenv(key, default)





