from flask import Flask
app=Flask(__name__)

@app.route("/")
def calc1():
    num1=8
    num2=4
    sum1=num1+num2
    diff1=num1-num2
    prod1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    return str(12)
    #return(sum1,diff1,prod1,div1,div2,rem1,exp1)

if __name__=='__main__':
    app.run()
