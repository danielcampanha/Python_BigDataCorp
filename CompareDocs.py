## Read me ##
## This script was made to get 2 lists from 2 differents files and get the difference between then ##
def compareDocuments():

    smaller_list = []
    file = open("C:\Code\smaller_list.txt", "r")
    for item in file:
        smaller_list.append(item)

    list_all = []
    file_all = open("C:\Code\Bigger_list.txt", "r")
    for item in file_all:
        list_all.append(item)

    difference = []

    for total in list_all:
        for smaller_item in smaller_list:
            have = False
            if total == smaller_item:
                have = True
                break
        if have == False:
                difference.append(total)


    with open('list_avg.txt', 'w') as f:
        for item in difference:
            f.write(item)

if __name__ == "__main__":
    compareDocuments()