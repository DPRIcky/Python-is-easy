def drawfield():
    for row in range(11):
        if row%2 == 0:
            for column in range(13):
                if column%2 == 0:
                    if column != 12:
                        print(" ",end = "")
                    else:
                        print(" ")
                else:
                    print("|",end = "")
        else:
            print('-------------')

player = 1
currentfield = [[" "," "," "],[" "," "," "],[" "," "," "]]
while(True):
    print("Player",player,"turn")
    moverow = int(input("Enter the row: \n"))
    movecolumn = int(input("Enter the column: \n"))
    if player == 1:
        currentfield[movecolumn][moverow] = "X"
        player = 2
    else:
        currentfield[movecolumn][moverow] = "0"
        player = 1
    print(currentfield)

drawfield()
