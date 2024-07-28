#add import
from question_b import Stock

def main():
    info = Stock()
    print("Stock Report Menu")
    print("Option 1 : Apple Inc")
    print("Option 2 : Caterpillar")
    print("Option 3 : Eastman Kodak")
    print("Option 4 : Google")
    print("Option 5 : Microsoft")

    choice = int(input("Which company do you want to know about? : "))

    if choice >= 1 and choice <= 5: 
        print("Company Symbol : ",info.get_symbol(choice-1), "Company Name : ",info.get_company_name(choice-1))

main()