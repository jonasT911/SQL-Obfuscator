import sys


print("Begin Obfuscator")

SQLcommands = ['\' OR 1=1#']

def createTautology():
    listOfTauts= ['0','2/2-1','8-8','COS(PI()/2)','SIN(0)']
    #Randomly select value
    return str(listOfTauts[0]) +" = " +str(listOfTauts[1])
    
def obfuscateCommand(string):
    value=createTautology()
    output = string +' '+value + ' #'
    return output
    
outputCommand = obfuscateCommand(sys.argv[1])

print(outputCommand)