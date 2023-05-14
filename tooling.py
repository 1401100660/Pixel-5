import random

def writeFiles(file_name, text):
    try: 
        with open(file_name, "a") as f:
            f.write(text)
    except FileNotFoundError:
        with open(file_name, "w") as f:
            f.write(text)
def readFiles(file_name, text):
    try:
        with open(file_name, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "no file found"

