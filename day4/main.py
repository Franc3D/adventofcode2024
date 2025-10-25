
def main():
    
    #Create a list of list so that we can access the specific data we want using list[x][y]
    word = "XMAS"

    table = fill_table("file.txt")
    number_of_rows = len(table)
    number_of_columns = len(table[0]) - 1
    #print(number_of_rows, "-", number_of_columns)

    total_word_found = 0
    
    for row in range(0, number_of_rows):
        print("This is the row # ", row)
        for column in range(0, number_of_columns):
            print("This is the column # ", column)

            if table[row][column] == word[0]:
                total_word_found += find_all_words(table, [row, column], word)
    
    print("The total amount of the word found is : ", total_word_found)
    """

    

                                            # Start is -1, -1 compared to notepad with cursor in front
    print(f"There are {find_all_words(table, [0, 136], word)} words found at that start location")
    """
    
    """
    print("******")
    answer = find_key_word(table, [0,6], [0,1])
    print("The verified portion is :", answer)
    """
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
    
    #From the start location list, search in the direction and return true if the keyword is found
    
    locator = [start[0], start[1]]
    for char in keyword:
        #print(table[locator[0]][locator[1]] , char) #To visualise the comparaison
        if table[locator[0]][locator[1]] != char:
            return False
        
        #move on to the next char to check on the list
        locator[0] += direction[0]
        locator[1] += direction[1]

        
    return True

def find_all_words(table, start, keyword="XMAS"):

    words_found = 0

    #Verify if the edges of the table are at the distance len(keyword)
    number_of_rows = len(table) - 1
    number_of_columns = len(table[0]) - 2

    #Knowing that he start position does not change until the function is called again
    #Do the following verifications 
    row_range = [-1, 1]
    column_range = [-1, 1]

    #ROW OUT OF BOUND CHECK
    #if the row goes out of range upward
    if start[0] - (len(keyword)-1) < 0:
        print("Restricted top")
        row_range[0] = 0 #avoid checking the top   
    #If the row goes out of range downward
    if start[0] + (len(keyword)-1) > number_of_rows:
        print("Restricted bottom")
        row_range[1] = 0 #avoid checking the bottom

    #COLUMN OUT OF BOUNDS CHECK
    #if the column goes out of range left 
    if start[1] - (len(keyword) - 1) < 0:
        print("Restricted left")
        column_range[0] = 0 #avoid checking the left
    #if the column goes out of range right
    if start[1] + (len(keyword) - 1) > number_of_columns:
        print("Restricted right")
        column_range[1] = 0 #avoid checking the right
    
    #Verify every angles that are valid 
    for row_direction in range(row_range[0], row_range[1]+1):

        for column_direction in range(column_range[0], column_range[1]+1):

            #in case of direction 0, 0 SKIP because it goes nowhere
            if row_direction == 0 and column_direction == 0:
                continue

            print("vvv Row direction :", row_direction, " | Column direction :", column_direction)
            
            #add +1 to the counter if find_key_word() return True
            if find_key_word(table, start, [row_direction, column_direction]):
                words_found += 1
            
            

    return words_found



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