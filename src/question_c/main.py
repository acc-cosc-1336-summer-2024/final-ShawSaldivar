#add import
import question_c

def main():
    elements  = []
    for i in range(5):
        x = int(input(f"Enter the {i+1} number: "))
        elements.append(x)
    question_c.get_numbers(elements)
    
main()