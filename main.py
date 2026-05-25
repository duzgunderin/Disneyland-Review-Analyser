import process
import tui
import visual
from review import Review

#controls the view data sub-menu
def handle_view_data_menu(reviews):
    back_to_main = False
    while not back_to_main:
        tui.display_view_data_menu()
        choice = tui.get_user_choice()

        if choice == "A" :
            park_name = tui.get_park_name()

            matching_reviews = process.get_reviews_by_park(reviews, park_name)
            tui.display_reviews(matching_reviews)

        elif choice == "B" :
            park_name = tui.get_park_name()

            location = tui.get_location()

            review_count = process.count_reviews_by_location(reviews, park_name, location)

            print(f"Number of reviews: {review_count}")

        elif choice == "C" :
            process.export_summary(reviews)

        elif choice == "D" :
            print("Average score by location selected")

        elif choice == "X" :
            back_to_main = True

        else:
            tui.display_invalid_choice()

#controls the visualize data sub-menu
def handle_visualise_menu(reviews):
    back_to_main = False
    while not back_to_main:
        tui.display_visualise_menu()
        choice = tui.get_user_choice()

        if choice == "A" :
            park_counts = process.count_reviews_per_park(reviews)
            visual.show_most_reviewed_park(park_counts)

        elif choice == "B" :
            park_name = tui.get_park_name()

            top_locations = process.get_top_10_locations_by_average_rating(reviews, park_name)

            visual.show_top_10_locations(top_locations, park_name)

        elif choice == "C" :
            park_name = tui.get_park_name()

            month_averages = process.get_average_rating_by_month(reviews, park_name)

            print(month_averages)

            visual.show_average_rating_by_month(month_averages, park_name)

        elif choice == "X" :
            back_to_main = True

        else:
            tui.display_invalid_choice()

#main function that controls the program flow
def main():

#load the dataset

    reviews = process.load_reviews("data/Disneyland_reviews.csv")

    tui.display_title()
    tui.display_dataset_loaded(len(reviews))

    sample_review = Review("Disneyland_Paris", "UK", 5, "2019-4" )
    sample_review.display_reviewee()

    running = True
#Main program loop
    while running:
        tui.display_main_menu()
        choice = tui.get_user_choice()

        if choice == "A":
            handle_view_data_menu(reviews)
        elif choice == "B":
            handle_visualise_menu(reviews)
        elif choice == "C":
            process.export_summary(reviews)
        elif choice == "X":
            print("Program closed.")
            running = False
        else:
            tui.display_invalid_choice()

if __name__ == "__main__":
     main()



