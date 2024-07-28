#add import
from question_a import Stock

def main():
    s = Stock()
    print("1 : Stock Purchase History")
    print("2 : Exit")

    choices = int(input("Your Option : "))

    while(choices != 2):

        if choices == 1:
            s.stock_purchase_history()            
        else:
            print("Invalid option, please try again")

        print("\n1 : Stock Purchase History")
        print("2 : Exit")

        choices = int(input("Your Option : "))

main()
