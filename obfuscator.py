import sys


print("Begin Obfuscator")

SQLcommands = ['\' OR 1=1#']

def createTautology():
    listOfTauts= ['0','2/2-1','8-8','COS(PI()/2)','SIN(0)']
    #Randomly select value
    return str(listOfTauts[0]) +" = " +str(listOfTauts[1])
    
def changeLogicOperations (): #Randomly chooses between written and signs, and adds extra meaningless extensions.
        pass

def obfuscateCommand(string):
    sections=string.split("\'")
    output = ""
    for i in range(len(sections)):
        if(i%2==1):
            loopTemp=""
            terms=sections[i].split(" ")
            print(terms)
            for term in terms:
                if ("=" in term):
                    print("Term is "+str(term))
                    loopTemp+=" "+str(createTautology())
                else:
                    loopTemp+=term
        else:
            loopTemp=str(sections[i])
        if(i<len(sections)-1):   
            loopTemp+="\'"
        output+=loopTemp
    output+="#"
    return output
    
    
    
outputCommand = obfuscateCommand(sys.argv[1])

print(outputCommand)