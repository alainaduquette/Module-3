import csv

#open the csv
with open("C:\\Users\\alain\\Documents\\Bootcamp\\Python Challenge\\Python-Challenge\\PyRoll\\Resources\\election_data.csv", "r") as file:
    #read the first line
    header=file.readline()
    #set the name of my readr 
    my_reader = csv.reader(file, delimiter=",")
    #create a dictionary to begin adding to
    candidate_dictionary = {}
    
    #create a list that allows to later turn into a count of total
    ballot_id = []

    #create a for loop that runs through all lines in the csv
    for row in my_reader:
        #states the column which cadidate name is 
        candidate_name = row[2]
        #states if the candidate is not already in the dictionary add the candidate and set the total count along with it to 0
        if candidate_name not in candidate_dictionary.keys():
            candidate_dictionary[candidate_name] = 0
         
         #if the candidate name is in the dictionary than add 1 to the count
        candidate_dictionary[candidate_name] = candidate_dictionary[candidate_name] +1 
        #adding to the dic to count total
        ballot_id.append({'county':row[1], 'candidate':row[2]})
        
count = len(ballot_id)

#create a new list for the percent
total_percent = []
#create a for loop to go through the csv to then add the percents
for votes_cast in candidate_dictionary.values():
    total_percent.append(round(((votes_cast / count)*100), 3))
#
total_percent_index=0

print("Election Resuluts")
print("------------------------------------------------")
print("Total Votes: " + str(count))
print("------------------------------------------------")
for candidate_name, votes_cast in candidate_dictionary.items():
   

    print(candidate_name +": " + str(total_percent[total_percent_index]) + "% " +"("+ str(votes_cast) +")")
    total_percent_index=total_percent_index+1

print("------------------------------------------------")

print("Winner: " + max(candidate_dictionary, key=candidate_dictionary.get), max(candidate_dictionary.values()))
print("------------------------------------------------")






    




