from flask import Flask
app=Flask(__name__)

@app.route("/")
def calc1():
    print(12)
    return str(8+4)
if __name__=="__main__":
    app.run()
