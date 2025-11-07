


def main():
    

    compare_list, page_list = split_data_in_lists()

    valid_set_pages = 0

    for pages_string in page_list:
        page_valid = True
        pages = pages_string.split(",")
        compare_invalid = ""

        for compare in compare_list:
            if is_following_rules(compare, pages_string) == False: 
                compare_invalid = compare
                page_valid = False
                break

        print("The pages", pages_string, end=" are ")
        if page_valid:
            print("VALID, adding", pages[int(len(pages)//2)], "to the total")
            valid_set_pages += int(pages[int(len(pages)//2)])
        else:
            print("INVALID due to the comparaison", compare_invalid)
            continue
    
    print("The total of all the middle values of the valid page groups is", valid_set_pages)
        



def is_following_rules(compare, pages_string):

    #split the compare string into the before and after 
    before, after = compare.split("|")

    location_before = pages_string.find(before)
    location_after = pages_string.find(after)

    if location_before == -1 or location_after == -1:
        return True
        
    else:
        
        if location_before < location_after:
            return True
        else:
            return False

    #could use pages_string instead and do a find() to see if the returned value is <=> compared to the 2nd compare


def split_data_in_lists(verbose = False):
    compare_list = []
    page_list = []

    #Read the document and store its content in 2 different lists
    with open("input.txt", "r") as f:
        lines = f.readlines()

        #for each line, if | is present add to the compare list
        for line in lines:
            #Go over all the useless lines
            if line.isspace():
                continue
            line = line.strip()

            if line.find("|") >= 0:
                compare_list.append(line)
            else:
                page_list.append(line)


    if verbose:
        print("List of comparaisons : ")
        for item in compare_list:
            print(item)
        print("\nList of pages : ")
        for item in page_list:
            print(item)

    return compare_list, page_list


if __name__ == "__main__":
    main()