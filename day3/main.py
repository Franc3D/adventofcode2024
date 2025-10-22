
def main():

    with open("corrupted_file.txt") as f:
        
        for line in f.readlines():
            
            next_mul = line.find("mul(")

            
    #Find the word mul
    #see if next is ( 
    #check for numbers up to 3 times and also look for , after the 1st time
    # it should go from mul(#,#) to mul(###,###)



if __name__ == "__main__":
    main()