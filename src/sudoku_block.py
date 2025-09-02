# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    count1=0
    count2=0
    column=[]
    for val in sudoku:
        count2=0
        for valu in val:
            if(count1 >= row_no and count1 < row_no +3 and count2 >= column_no and count2<column_no+3):
                column.append(valu)
            count2+=1
        count1+=1
    print(column)

    count1 = 0
    count2 = 0
    for num in column:
        count1 += 1
        for nom in column:
            count2+=1
            if nom == num and nom != 0 and num != 0 and count1 != count2:
                return False
        count2 = 0
    return True

if __name__ == "__main__":
 
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))