from random import randint

def checkChosenNumbers(chosenNumbers):
    if(len(chosenNumbers) > 10 or len(chosenNumbers) == 0):
       raise Exception("ERROR: Too many or too few chosen numbers.")
    if len(set(chosenNumbers)) != len(chosenNumbers):
        raise Exception("ERROR: Duplicate values.")
    for x in chosenNumbers:
        if(x > 90 or x < 1):
           raise Exception("ERROR: Some chosen numbers are out of range (1,90)")

def generateRandomNumbers():
    extractedNumbers = set()
    while len(extractedNumbers) < 20:
        extractedNumbers.add(randint(1, 90))
    return extractedNumbers

def generateSummary(chosenNumbers):
    result = dict()
    for x in range(0,len(chosenNumbers) + 1):
       result[x] = 0
    return result

def printSummary(winningsSummary,chosenNumbers,extractionTimes):
    file = open("Winnings_Summary.txt","w")
    file.write(("Here is your summary! You chose " + str(len(chosenNumbers)) + " numbers for " 
    + str(extractionTimes) + " extractions."  + " The results: \n\n"))
    
    for key in winningsSummary:
        file.write("- Guessed " + str(key) + " numbers " + str(winningsSummary[key]) + " times \n")

    file.close
