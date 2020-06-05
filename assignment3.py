def equality(num1,num2,num3):
    if int(num1) == int(num2) or int(num2) == int(num3) or int(num3) == int(num1):
        print(True)
    else:
        print(False)

equality(1,2,3)
equality(1,1,3)
equality(3,4,4)
equality(6,8,6)
equality(8,8,8)
equality("4",5,4)
equality("5",9,"5")
equality("5","9","7")
