from os import listdir 
def virusFinder():
    """
    Hello. i'am the virus finder of your
    monitor.    
    """
    for i in listdir():
        with open(i, "r") as file1:
            if file1.readline() == "Devil\n":
                return "/n/nyour computer has a virus!!"
            
Virus = virusFinder()
print(virusFinder.__doc__)
print(Virus)
