from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    import os
    f1 = open("old.txt",'r')
    list = []
    for i in f1:
        list.append(i)
    return list
if __name__ == '__main__':
    app.run()
