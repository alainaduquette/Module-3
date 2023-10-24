import csv

with open("C:\\Users\\alain\\Documents\\Bootcamp\\Python Challenge\\Python-Challenge\\PyBank\\Resources\\budget_data.csv", "r") as file:
    header=file.readline() 
    my_reader = csv.reader(file, delimiter=",")
    total = 0
    month_counter = 0
    sum = 0
    changedict={}
    
    for date,profit in my_reader:
        if (month_counter == 0):
            temp = int(profit)
        else:
            changedict[date] = int(profit) - temp
            temp = int(profit)
        
        month_counter = month_counter + 1

        total = total + int(profit)


f"Financial Analysis"
f"----------------------------"
f"Total Months: " + str(month_counter)
f"Total: " + str(total)
"Average Change: " + str(int(total) / int(len(changedict)))
"Greatest Increase in Profits: " + max(changedict, key=changedict.get), max(changedict.values()))
print("Greatest Decrease in Profits: " + min(changedict, key=changedict.get), max(changedict.values()))
