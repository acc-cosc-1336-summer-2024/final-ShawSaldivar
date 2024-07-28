#add import
import question_d

def main():
    print("Multiplication Displayer")
    print(" 1 : Display Multiplication Table ")
    print(" 2 : Exit ")

    choices = int(input("What Would You Like to Do? : "))

    while(choices != 2):
        if(choices == 1):
            table = question_d.create_multiplication_table()
            question_d.display_multiplication_table(table)
        print("\nMultiplication Displayer")
        print(" 1 : Display Multiplication Table ")
        print(" 2 : Exit ")

        choices = int(input("What Would You Like to Do? : "))

main()