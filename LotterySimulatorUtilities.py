from random import randint

#Check input
def checkIfNumeric(intValue):
    try:
        intValue = int(intValue)
        return intValue
    except ValueError:
        raise Exception("ERROR: Input is not a number")

def checkChosenNumbers(numbersInput):
    if(checkSpaces(numbersInput)):
        chosenNumbersArr = str(numbersInput).split(",")

        for x in chosenNumbersArr:
            checkIfNumeric(x)

    chosenNumbersArr = [int(i) for i in chosenNumbersArr]
    if(len(chosenNumbersArr) > 10 or len(chosenNumbersArr) == 0):
       raise Exception("ERROR: Too many or too few chosen numbers.")
    if len(set(chosenNumbersArr)) != len(chosenNumbersArr):
        raise Exception("ERROR: Duplicate values.")
    for x in chosenNumbersArr:
        if(x > 90 or x < 1):
           raise Exception("ERROR: Some chosen numbers are out of range (1,90)")

    return chosenNumbersArr


#Check input
def checkSpaces(numbersInput):
    if (str(numbersInput).replace(" ","")):
        return True
    else:
        raise Exception("ERROR: Empty")


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

def getTkinterSummary(winningsSummary,chosenNumbers,extractionTimes):

    chosenNumbersAmount = str(len(chosenNumbers))
    amountOfExtractions = str(extractionTimes)

    result = str()

    result += (("Here is your summary!\n You chose " + chosenNumbersAmount + " numbers for " 
    + amountOfExtractions + " extractions."  + " The results: \n"))
    
    for key in winningsSummary:
        winningsAmount = str(winningsSummary[key])
        keyStr = str(key)

        
        percentage = str(round(((float(winningsAmount) / int(amountOfExtractions)) * 100),2))

        result +=  ("- Guessed " + keyStr + " numbers " + winningsAmount + " times ( " + percentage + "% ) \n")

    return result



def printSummary(winningsSummary,chosenNumbers,extractionTimes):

    chosenNumbersAmount = str(len(chosenNumbers))
    amountOfExtractions = str(extractionTimes)

    file = open("./ExtractionsSummary.txt","w")
    file.write(("Here is your summary! You chose " + chosenNumbersAmount + " numbers for " 
    + amountOfExtractions + " extractions."  + " The results: \n\n"))
    
    for key in winningsSummary:
        winningsAmount = str(winningsSummary[key])
        keyStr = str(key)

        
        percentage = str(round(((float(winningsAmount) / int(amountOfExtractions)) * 100),2))

        file.write("- Guessed " + keyStr + " numbers " + winningsAmount + " times ( " + percentage + "% ) \n")

    file.close
