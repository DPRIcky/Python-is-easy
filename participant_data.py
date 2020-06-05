# participant_number = 5
# participant_data = []
# registered_participants = 0
# output_file = open("Participant Data.txt","w")

# while(registered_participants < participant_number):
#     temppartdata = [] #name,country of origin, age
#     name = input("Please enter your name: ")
#     temppartdata.append(name)
#     country = input("Please enter your country of origin: ")
#     temppartdata.append(country)
#     age = int(input("Enter your age: "))
#     temppartdata.append(age)
#     print(temppartdata)
#     participant_data.append(temppartdata)
#     print(participant_data)

#     registered_participants += 1

# for participant in participant_data:
#     for data in participant:
#         output_file.write(str(data))
#         output_file.write(" ")
    
#     output_file.write("\n")

# output_file.close()

input_file = open("Participant Data.txt","r")
input_list = []
for line in input_file:
    tempparticipant = line.strip("\n").split()
    input_list.append(tempparticipant)
    print(input_list)
    
Age = {}
for part in input_list:
    tempage = int(part[-1])
    if tempage in Age:
        Age[tempage] += 1
    else:
        Age[tempage] = 1

print(Age)

oldest = 0
youngest = 100
mostoccurringage = 0
counter = 0

for tempAge in Age:
    if tempAge > oldest:
        oldest = tempAge
    if tempAge < youngest:
        youngest = tempAge
    if Age[tempAge] >= counter:
        counter = Age[tempAge]
        mostoccurringage = tempAge

print(oldest)
print(youngest)
print("most occuring age is", mostoccurringage, "with", counter, "participants")

input_file.close()