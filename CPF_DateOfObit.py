
## Read me ##
## This script was made to take from a file with format [CPF | DATE], get the month of the DATE ##

def MonthFromDate():
    nova_lista_date = []
    dates = open("C:\Code\month.txt", "r")
    for date in dates:
        temp = date.split("|")
        month = temp[2][2:4]
        new_date = str(temp[0]+"|"+temp[1]+"|"+month+"|"+temp[2])
        nova_lista_date.append(new_date)


    with open('Result.txt', 'w') as f:
        for item in nova_lista_date:
            f.write(str(item))

if __name__ == "__main__":
    MonthFromDate()