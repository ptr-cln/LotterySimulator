from LotterySimulatorUtilities import *

chosenNumbers = checkChosenNumbers([1,10,20,30,40,50,60,70,80,90])
extractionTimes = checkIfNumeric(1000)

winningsSummary = generateSummary(chosenNumbers)

checkChosenNumbers(chosenNumbers)

for x in range(0,extractionTimes):
    
    generatedNumbers = generateRandomNumbers()
    print("Extracted Numbers = " , generatedNumbers)

    guessedIt = 0

    for i in chosenNumbers:
        if (i in generatedNumbers):
            guessedIt = guessedIt + 1
    
    winningsSummary[guessedIt] = winningsSummary[guessedIt] + 1


printSummary(winningsSummary,chosenNumbers,extractionTimes)
