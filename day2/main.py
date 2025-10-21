

def main():
    safe_report_count = 0

    with open("reports.txt") as f:
        for row in f:
            data = row.split()

            previous_n = 0
            increasing = None
            invalid_threshold = 1
            invalid = 0
            for x, n in enumerate(data):
                n = int(n)
                if x == 0:
                    print("is first number", n)
                    #previous_n = n
                elif x == 1:
                    print("is second number", n, previous_n)
                    if abs(n - previous_n) > 0 and abs(n - previous_n) < 4:
                        if n > previous_n:
                            increasing = True
                        else:
                            increasing = False
                    else:
                        invalid += 1
                else: #if we know the 
                    print("in complete comparations", n, previous_n)
                    if abs(n - previous_n) > 0 and abs(n - previous_n) < 4:
                        if increasing and n < previous_n:
                            invalid += 1
                        elif increasing is False and n > previous_n:
                            invalid += 1
                    else:
                        invalid += 1
                    #Verify if the numbers are increasing or decreasing
                    #True if increasing, False if decreasing
                
                previous_n = n

            if invalid < invalid_threshold:
                print("plus one report confirmed")
                safe_report_count += 1
            
            invalid = False

    print(safe_report_count)





    # Given a given amount of columns separated by spaces

    #We want to know whick reports are SAFE
    #Safe means either steadily increasing or decreasing
    #2 adjacent levels must differ by at least 1 and at most 3

    #Return the amount of safe reports

if __name__ == "__main__":
    main()