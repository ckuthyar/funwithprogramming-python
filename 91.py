#Malware which will steal all the email addresses
#in my laptop and send it to China
#show it in http://127.0.0.1:5000

import os
from flask import Flask,render_template
app=Flask(__name__)

@app.route("/malware")
def malware1():
    list1=[]
    info1=os.listdir()
    print(info1)
    f1=info1[99]
    print("File name is ..................:", f1)
    c1=open(f1,"r")
    flag=True
    while flag==True:
        info=c1.readline()
        list1.append(info)
        if info=="":
            flag=False
        
    print(list1)
    return render_template("malware1.html",param1=list1)

if __name__=="__main__":
    app.run()


