def cfile(name):
    with open(name, "x") as h:
     name = str(name)

def rfile(name):
    name = str(name)
    content = open(name, "r")
    return content

def wfile(name, content):
    name = str(name)
    content = str(content)
    Write = open(name, "w")
    Write.write(content)

def afile(name, content):
    name = str(name)
    content = str(content)
    Append = open(name, "a")
    Append.write(content)

cfile("Chandra.txt")
result=rfile("Chandra_2.txt")
print(result)
