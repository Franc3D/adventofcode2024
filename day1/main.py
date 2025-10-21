"""
Day 1:historian Hysteria

take 2 lists with numbers in random order and compare the lowest number of both, then the nextt lowest


"""

def main():
    number_difference = 0
    list1 = []
    list2 = []

    #Get the list from lists.txt and divide the content into 2 different lists
    with open("lists.txt") as f:
        for line in f:
            lines = line.split("   ")
            list1.append(lines[0])
            list2.append(lines[1])

    #Reorder each lists from lowest to highest
    list1.sort()
    list2.sort()

    #Compare 
    for x, n in enumerate(list1): #same length list
        print(f"lists: {list1[x]} - {list2[x].strip()}")
        difference = int(list1[x]) - int(list2[x])
        print(f"difference : {difference}")
        number_difference += abs(difference)
        print(f"New total : {number_difference} \n")
        
    
    print(number_difference)


if __name__ == "__main__":
    main()