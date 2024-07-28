#write functions here, don't add input('') statements here!

def create_multiplication_table():
    table = []


    for r in range(1 , 6):
        row_list = []
        for c in range(1, 11):
            row_list.append((r)*(c))
        table.append(row_list)
    return table

def display_multiplication_table(list):
    for r in range(5):
        for c in range(10):
            print(list[r][c]," ",end="")
        print("")