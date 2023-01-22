sudoku=[[0,0,0,2,6,0,7,0,1],
       [6,8,0,0,7,0,0,9,0],
       [1,9,0,0,0,4,5,0,0],
       [8,2,0,1,0,0,0,4,0],
       [0,0,4,6,0,2,9,0,0],
       [0,5,0,0,0,3,0,2,8],
       [0,0,9,3,0,0,0,7,4],
       [0,4,0,0,5,0,0,3,6],
       [7,0,3,0,1,8,0,0,0]]
rows = 9
columns = 9

def findNum():
    tempList =[1,2,3,4,5,6,7,8,9]
    for i in range(rows):
        for j in range(columns):
            subrow = i
            subcolumn = j
            if sudoku[i][j] == 0:
                for subrow in range(columns):
                    match sudoku[subrow][j]:
                        case 1:
                            try:
                                tempList.remove(1)
                            except:
                                pass
                                #print("already found")
                        case 2:
                            try:
                                tempList.remove(2)
                            except:
                                pass
                                #print("already found")
                        case 3:
                            try:
                                tempList.remove(3)
                            except:
                                pass
                                #print("already found")
                        case 4:
                            try:
                                tempList.remove(4)
                            except:
                                pass
                                #print("already found")
                        case 5:
                            try:
                                tempList.remove(5)
                            except:
                                pass
                                #print("already found")
                        case 6:
                            try:
                                tempList.remove(6)
                            except:
                                pass
                                #print("already found")
                        case 7:
                            try:
                                tempList.remove(7)
                            except:
                                pass
                                #print("already found")
                        case 8:
                            try:
                                tempList.remove(8)
                            except:
                                pass
                                #print("already found")
                        case 9:
                            try:
                                tempList.remove(9)
                            except:
                                pass
                                #print("already found")
                for subcolumn in range(rows):
                    match sudoku[i][subcolumn]:
                        case 1:
                            try:
                                tempList.remove(1)
                            except:
                                pass
                                #print("already found")
                        case 2:
                            try:
                                tempList.remove(2)
                            except:
                                pass
                                #print("already found")
                        case 3:
                            try:
                                tempList.remove(3)
                            except:
                                pass
                                #print("already found")
                        case 4:
                            try:
                                tempList.remove(4)
                            except:
                                pass
                                #print("already found")
                        case 5:
                            try:
                                tempList.remove(5)
                            except:
                                pass
                                #print("already found")
                        case 6:
                            try:
                                tempList.remove(6)
                            except:
                                pass
                                #print("already found")
                        case 7:
                            try:
                                tempList.remove(7)
                            except:
                                pass
                                #print("already found")
                        case 8:
                            try:
                                tempList.remove(8)
                            except:
                                pass
                                #print("already found")
                        case 9:
                            try:
                                tempList.remove(9)
                            except:
                                pass
                                #print("already found")
                if len(tempList) == 1:
                    sudoku[i][j]=tempList[0]
                    return 
                elif len(tempList) == 0:
                    sudoku[i][j]=0
                    return tempList.pop()
                else:
                    for index in range(len(tempList)):
                        sudoku[i][j]=tempList[index]
                        print(sudoku)
                        findNum()
               



findNum()
print(sudoku)