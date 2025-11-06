


def main():
    

    compare_list, page_list = split_data_in_lists()

    valid_set_pages = []

    for pages_string in page_list:
        page_valid = True
        pages = pages_string.split(",")

        for compare in compare_list:
            if is_following_rules(compare, pages) == False: #NEED TO FINISH THIS FUNCTION
                page_valid = False
                break
        
        if page_valid:
            valid_set_pages.append(pages)
        else:
            continue
        



def is_following_rules(compare, pages):

    #split the compare string into the before and after 
    before, after = compare.split("|")


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