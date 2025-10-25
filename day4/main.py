
def main():
    
    #Create a list of list so that we can access the specific data we want using list[x][y]
    table = fill_table("file.txt")
    number_of_rows = len(table) -1
    number_of_columns = len(table[0]) - 2
    print(number_of_rows, "-", number_of_columns)
    
    print("******")
    answer = find_key_word(table, [0,6], [0,1])
    print("The verified portion is :", answer)

    #Need to create a function that checks directions from -1, -1 to 1, 1 while ignoring 0, 0
    #The function need to return the number of valid discovered (8 max per run)
    #The function needs to check the bounds and skip that direction if it were to go out of bounds
    

    """
    #To test a specific letter in the table
    number1 = input("Enter the row number : ")
    number2 = input("Enter the column number : ")

    print("Your result is : ", table[int(number1)][int(number2)])
    """

def find_key_word(table, start, direction, keyword="XMAS"):
    number_of_rows = len(table) -1
    number_of_columns = len(table[0]) - 2
    #From the start location list, search in the direction and return true if the keyword is found
    
    locator = [start[0], start[1]]
    for char in keyword:
        if table[locator[0]][locator[1]] != char:
            print(table[locator[0]][locator[1]] , char)
            return False
        
        #move on to the next char to check on the list
        locator[0] += direction[0]
        locator[1] += direction[1]
    
    return True

    

def fill_table(file_name):
    table = []

    #read file.txt and fill the table char by char, then row by row
    with open(file_name) as f:
        for row in f.readlines():
            #for each row create a row_list and apply it to table
            row_list = []
            for char in row:
                row_list.append(char)
            table.append(row_list)
    
    return table


if __name__ == "__main__":
    main()