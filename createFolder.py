import os

def createFolder():
    if not os.path.exists("images"):
        os.makedirs("images")