# PROJECT: READING LIST

reading_list = []

menu_prompt = """Enter one of the following options:
    'a' to add a book
    'l' to list the books
    'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()

def add_book():
    print("Adding...")
    title = input("Enter book title: ").strip().title()
    author = input("Enter author's name: ").strip().title()
    year = input("Enter year of publication: ").strip().title()

    new_book = {                    # Add user inputs to dictionary
        "title": title,             # The 2nd title refers to the title variable above (input)
        "author": author,
        "year": year
    }

    reading_list.append(new_book)   # append dictionary to reading_list


def show_books():
    print("Displaying...")
    for book in reading_list:
        title, author, year = book.values()     # use unpacking and the dictionary's .values() method to make code clearer
        print(f"{title}, by {author} ({year})")


while selected_option != "q":
    if selected_option == "a":
        add_book()                  # appends
    elif selected_option == "l":
        if reading_list:            # passes reading_list to the bool() function: True if not empty; otherwise False.
            show_books()            # prints
        else:
            print("Your reading list is empty.")
    else:
        print(f"Sorry, '{selected_option}' is not a valid option.")

    # Allow user to change their selection after every iteration:
    selected_option = input(menu_prompt).strip().lower()
else:
    print("Bye")

print(f"List: {reading_list}")
