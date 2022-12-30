#!/usr/bin/env python3


# Created by: Peter Sobowale
# Created on: Dec 29 2022
# This program gets 2 lists of numbers and combines them


def alternating_elements(list1, list2):
    # Create an empty result list
    result = []

    # Zip together the two lists and iterate through them

    for element1, element2 in zip(list1, list2):
        # Append the elements to the result list, alternating between them
        result.append(element1)
        result.append(element2)

    return result


# Main function
def main():
    # User interface
    print(
        "This program asks the user to enter 2 lists of different elements. It then displays the new list with alternating elements.\n"
    )

    # Prompt the user to enter the first list
    list1_str = input("Enter a list of elements, separated by spaces: ")

    # Split the string into a list of elements
    list1 = list1_str.split(" ")

    # Prompt the user to enter the second list
    list2_str = input("Enter a second list of elements, separated by spaces: ")

    # Split the string into a list of elements
    list2 = list2_str.split(" ")

    # formatting
    print()

    # erroneous data
    if len(list1) != len(list2):
        print("Both lists must have the same number of elements.")
    else:
        # Call the alternating_elements function to get the final list
        result = alternating_elements(list1, list2)

        # Print the final list
        print("Both lists combined:", end=" ")
        print(result)


# Call the main function
if __name__ == "__main__":
    main()
