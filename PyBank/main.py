import os
import csv

filepath = os.path.join('/Users/aurelianfousse/Desktop/UCSD Bootcamp/Homework/Homework 3 - Python 1/python-challenge/PyBank/Resources/budget_data.csv')
with open(filepath, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')

    next(csv_reader)
# the total number of month
    totalMonths = 0
    
    totalPL = 0
    
    totalPLDelta = 0
    lastPL = None

    greatestIncrease = 0
    greatestIncreaseMonth = "bad"

    worstIncrease = 0
    worstIncreaseMonth = "bad"

    for row in csv_reader:
        totalMonths+=1
        
        date = row[0]
        profitLoss = int(row[1])
        
        totalPL+=profitLoss

        if (lastPL):
            currentPLDelta = profitLoss-lastPL
            totalPLDelta += currentPLDelta

            if (currentPLDelta > greatestIncrease):
                greatestIncreaseMonth = date
                greatestIncrease = currentPLDelta

            if (currentPLDelta < worstIncrease):
                worstIncreaseMonth = date
                worstIncrease = currentPLDelta

        lastPL = profitLoss # why does this have to be here?
        averagePL = totalPL/totalMonths
        print(date)
        print(profitLoss)

    print("Financial Analysis")
    print("----------------------------")

    print(f"Total Months: {totalMonths}")

    print(f"Total: ${totalPL}")

    averageDelta = totalPLDelta/(totalMonths-1)
    print(f"Average Change: ${averageDelta}")

    print(f"Greatest Increase in Profits: {greatestIncreaseMonth} ${greatestIncrease}")

    print(f"Greatest Decrease in Profits: {worstIncreaseMonth} ${worstIncrease}")

outputfilepath = '/Users/aurelianfousse/Desktop/UCSD Bootcamp/Homework/Homework 3 - Python 1/python-challenge/PyBank/maintext.txt'
if os.path.isfile(outputfilepath):
    os.remove(outputfilepath)
with open(outputfilepath, 'a') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")

    f.write(f"Total Months: {totalMonths}\n")

    f.write(f"Total: ${totalPL}\n")

    
    f.write(f"Average Change: ${averageDelta}\n")

    f.write(f"Greatest Increase in Profits: {greatestIncreaseMonth} ${greatestIncrease}\n")

    f.write(f"Greatest Decrease in Profits: {worstIncreaseMonth} ${worstIncrease}")