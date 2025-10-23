
def main():

    mul_total = 0
    with open("corrupted_file.txt") as f:
        

        for line in f.readlines():
            pointer = 0#3219
            failure = False


            while True:
                #Find the next mul( in the text and cut everything to reach it
                old_pointer = pointer
                pointer = line[pointer:].find("mul(")
                if pointer == -1:
                    break
                pointer += old_pointer
                print("*********")
                print("Pointer :", pointer) 

                #exit if there is no more instance of mul( to find
                
                
                #Get the next 12 char (longest possible)
                print("Char sequence :", line[pointer:pointer + 12])

                #Get the , location (if no , fail) (0 = 5 and 2 = 7)
                comma_location = line[pointer:pointer + 12].find(",")
                print("Comma_location :", comma_location)
                if not (comma_location >= 5 and comma_location <=7):
                    print(f"Failure, the comma location{comma_location} is misplaced or absent")
                    failure = True

                #Get the ) location (if no ) fail)
                close_location = line[pointer:pointer +12].find(")")
                print("Close bracket location", close_location)
                if not (close_location >= comma_location + 2 and close_location <= comma_location + 4):
                    print(f"Failure, the close bracket location{close_location} is misplaced or absent")
                    failure = True
                
                #is the content of the space between mul( and , a number ?
                number1 = line[pointer+4:pointer+comma_location]
                print("is num1 a number :", number1)
                if not number1.isnumeric():
                    print(f"Failure, the first number {number1} is not a number")
                    failure = True

                #is the content of the space between , and ) a number ?
                number2 = line[pointer+comma_location+1:pointer+close_location]
                print("is num2 a number :", number2)
                if not number1.isnumeric():
                    print(f"Failure, the second number {number2} is not a number")
                    failure = True

                if failure is False:
                    mul_total += int(number1) * int(number2)
                    

                pointer += 1
                failure = False
            
    print("Total of added multiplications :", mul_total)
    #Find the word mul
    #see if next is ( 
    #check for numbers up to 3 times and also look for , after the 1st time
    # it should go from mul(#,#) to mul(###,###)



if __name__ == "__main__":
    main()