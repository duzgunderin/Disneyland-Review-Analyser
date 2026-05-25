#display the program title
def display_title():
    print('Disneyland Review Analyser')

#display information about the loaded dataset
def display_dataset_loaded(row_count):
    print("Dataset loaded successfully")
    print(f"{row_count} rows loaded")

#display the main menu to the user
def display_main_menu():
    print("\nPlease enter one of the following options:")
    print("[A] View data")
    print("[B] Visualise data")
    print("[C] Export data")
    print("[X] Exit")

#gets user choice
def get_user_choice():

    return input("Please enter your choice: ").strip().upper()

def display_invalid_choice():
    print("Invalid choice. Please try again.")

#displays the view data sub-menu options
def display_view_data_menu():
    print("\nView Data Menu")
    print("[A] View all reviews for a park")
    print("[B] Number of reviews by park and reviewer location")
    print("[C] Average score for a park by year")
    print("[D] Average score per park by reviewer location")
    print("[X] Return to main menu")

#displays the visualize Data sub-menu options
def display_visualise_menu():
    print("\nVisualise Data Menu")
    print("[A] Most reviewed parks")
    print("[B] Park ranking by nationality")
    print("[C] Most popular month by park")
    print("[X] Return to main menu")

#gets the park name from the user
def get_park_name():

    return input("Please enter the park name: ")

#display the selected review
def display_reviews(reviews):

    for review in reviews:
        print(review)

#gets the reviewer location from the user
def get_location():

    return input("Please enter the reviewer location:")
