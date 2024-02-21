def main():
    # Prompting the user to enter a list of names
    names_input = input("Enter a list of names separated by spaces: ")

    # Splitting the input string into a list of names
    names_list = names_input.split()

    # Counting the total number of names entered by the user
    total_names = len(names_list)

    # Sorting the list of names alphabetically and removing duplicates
    unique_sorted_names = sorted(set(names_list))

    # Displaying the final sorted list of names
    print("Sorted list of unique names:")
    for name in unique_sorted_names:
        print(name)

    # Displaying the total number of names entered by the user
    print("Total number of names entered:", total_names)

if __name__ == "__main__":
    main()
