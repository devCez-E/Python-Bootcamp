from os import stat, stat_result


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
                    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
                    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
                    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", 
                    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
                    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
                    "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
                    "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", 
                    "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
                    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#Indexing
print(states_of_america[0])
print(states_of_america[-1])

#Change Values
states_of_america[1] = "Pencilvania"
print(states_of_america)

#Append
states_of_america.append("Cezannia")
print(states_of_america)