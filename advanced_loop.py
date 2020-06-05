def board(rows,clmn):
    if (rows<35 and clmn<35):
        if ((rows % 2 == 1 and clmn % 2 == 1) or (rows % 2 == 0 and clmn % 2 == 1)):
            for row in range(rows):
                if row%2 == 0:
                    for column in range(1,clmn+1):
                        if column % 2 == 1:
                            if column != clmn:
                                print(" ",end="")
                            else:
                                print(" ")
                        elif column % 2 == 0:
                            print("|",end = "")
                else:
                    print("-"*clmn)
            print(True)
    
    
        else:
            for row in range(rows-1):
                if row%2 == 0:
                    for column in range(1,clmn+1):
                        if column % 2 == 1:
                            if column != clmn:
                                print(" ",end="")
                        elif column % 2 == 0:
                            if column != clmn:
                                print("|",end = "")
                            else:
                                print("|")
                else:
                    print("-"*(clmn+1))
            print(True)
    else:
        print(False)


board(35,35)