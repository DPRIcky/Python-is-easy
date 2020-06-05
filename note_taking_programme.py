import os
file_name = input("Please enter the file name: ")
extention = input("Enter the file extention: ")
file_name = str(file_name) + str(extention)

try:
    old_file = open(str(file_name),"r")
    choice = input("What do you want to do?\nA) Read the file\nB) Delete the file and start over\nC) Append the file\nD) Replace a single line\nYour Choice (A/B/C/D): ")

    if (choice == 'A' or choice == 'a'):
        input_file = open(file_name,"r")
        input_list = []
        for line in input_file:
            tempparticipant = line.strip("\n").split()
            input_list.append(tempparticipant)
        print(input_list)
        
        input_file.close()
    
    elif (choice == 'B' or choice == 'b'):
        old_file.close()
        os.remove(file_name)
        open_file = open(str(file_name),"w")
        text = []
        temptext = input('Enter your text: ')
        text.append(temptext)
        question = input("Do you want to add more text (y/n)?: ")
        while(question != 'n'):
            temptext = input('Enter your text: ')
            text.append(temptext)
            print(temptext)
            print(text)
            question = input("Do you want to add more text (y/n)?: ")   
        for txt in text:
            open_file.write(str(txt))
            open_file.write(" ")
            open_file.write('\n')
        open_file.close()

    elif (choice == 'C' or choice == 'c'):
        open_file = open(file_name,'a+')
        text = []
        temptext = input('Enter your text: ')
        text.append(temptext)
        question = input("Do you want to add more text (y/n)?: ")
        while(question != 'n'):
            temptext = input('Enter your text: ')
            text.append(temptext)
            print(temptext)
            print(text)
            question = input("Do you want to add more text (y/n)?: ")   
        for txt in text:
            open_file.write(str(txt))
            open_file.write(" ")
            open_file.write('\n')
        open_file.close()

    elif (choice == 'D' or choice == 'd'):
        reading_file = open(file_name,"r")
        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            old_string = input("Enter the string to be replaced: ")
            new_string = input("Enter the string to be replaced with: ")
            new_line = stripped_line.replace(old_string, new_string)
            new_file_content += new_line +"\n"
        reading_file.close()

        writing_file = open(file_name, "w")
        writing_file.write(new_file_content)
        writing_file.close()
    

except FileNotFoundError:
    open_file = open(str(file_name),"w")
    text = []
    temptext = input('Enter your text: ')
    text.append(temptext)
    question = input("Do you want to add more text (y/n)?: ")
    while(question != 'n'):
        temptext = input('Enter your text: ')
        text.append(temptext)
        print(temptext)
        print(text)
        question = input("Do you want to add more text (y/n)?: ")   
    for txt in text:
        open_file.write(str(txt))
        open_file.write(" ")
        open_file.write('\n')
    open_file.close()
