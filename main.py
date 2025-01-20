#Main
from merge_sort import merge_sort
from merge_sort import merge

def main():
    print("Welcome to the Merge Sort Program!")
    while True:
        print("Options:")
        print("1. Generate a random list and sort it")
        print("2. Quit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "2":
            print("Goodbye!")
            break
        elif choice == "1":
            try:
                size = (input("Enter the size of the list: "))
                lower_bound =(input("Enter the lower bound: "))
                upper_bound = (input("Enter the upper bound: "))

                random_list = generate_random_list(size, lower_bound, upper_bound)
                print("\nGenerated List:")
                print_list(random_list)

                sorted_list = merge_sort(random_list)
                print("\nSorted List:")
                print_list(sorted_list)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please enter 1 or 2.")
