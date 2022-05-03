from tkinter import *
from turtle import width
from LotterySimulatorUtilities import *


def buttonClick():

    chosenNumbers = checkChosenNumbers(inputChosenNumbers.get())
    extractionTimes = checkIfNumeric(inputExtractionsAmount.get())

    winningsSummary = generateSummary(chosenNumbers)

    for x in range(0,extractionTimes):
    
        generatedNumbers = generateRandomNumbers()
        guessedIt = 0
        print("Extracted Numbers = " , generatedNumbers)    
        for i in chosenNumbers:
            if (i in generatedNumbers):
                guessedIt = guessedIt + 1
    
        winningsSummary[guessedIt] = winningsSummary[guessedIt] + 1

    summaryVar.set(getTkinterSummary(winningsSummary,chosenNumbers,extractionTimes))

    #Print the summary file only if the check "Generate Summary File" is true
    if(generateFileVar.get()):
        printSummary(winningsSummary,chosenNumbers,extractionTimes)



frame = Tk()
generateFileVar=BooleanVar()
summaryVar=StringVar()

frame.title("LotterySimulator")
frame.geometry("400x420")
frame.configure(background="#3e81c7")

labelChosenNumbers = Label(frame,text="Chosen Numbers (separated by comma):" , background="#3e81c7",font="MSSerif 13 bold")
labelChosenNumbers.pack(side="top",anchor=NW)

inputChosenNumbers = Entry(frame,width=500)
inputChosenNumbers.pack(side="top",padx=5, anchor=NW)
inputChosenNumbers.focus_set()

labelExtractionsAmount = Label(frame,text="Extractions Amount:" , background="#3e81c7",font="MSSerif 13 bold")
labelExtractionsAmount.pack(side="top",anchor=NW)

inputExtractionsAmount = Entry(frame,width=500)
inputExtractionsAmount.pack(side="top",padx=5, anchor=NW)

printFileCheckButton = Checkbutton(frame,text="Generate Summary File",onvalue=True,offvalue=False,variable=generateFileVar)
printFileCheckButton.pack(side="top",pady=10,padx=5,anchor=NW)

buttonExtract = Button(frame,text="Extract Numbers!",pady=5,command=buttonClick)
buttonExtract.configure(cursor ="hand2")
buttonExtract.pack()


labelTkinterSummary = Label(frame,textvariable=summaryVar,background="#3e81c7",font="Times 11 bold")
labelTkinterSummary.pack(side="bottom",anchor=NW)



frame.mainloop() 