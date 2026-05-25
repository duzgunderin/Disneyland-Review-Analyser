import matplotlib.pyplot as plt

#displays a pie chart showing the number of reviews per park
def show_most_reviewed_park(park_counts):

    labels = park_counts.keys()
    values = park_counts.values()

    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Number of Reviews per Disneyland Park")
    plt.show()

#displays a bar chart of the top 10 reviewer locations by average rating.
def show_top_10_locations(top_locations, park_name):

    locations = list(top_locations.keys())
    ratings = list(top_locations.values())

    plt.bar(locations, ratings)

    plt.title("Top 10 Locations")
    plt.xlabel("Reviewer Location")
    plt.ylabel("Average Rating")

    plt.xticks(rotation = 45)
    plt.tight_layout()

    plt.show()

#displays a bar chart showing average rating by month
def show_average_rating_by_month(month_averages, park_name):


    months = list(month_averages.keys())
    ratings =list(month_averages.values())

    plt.bar(months, ratings)

    plt.title(f"Average Rating by Month - {park_name}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.xticks(rotation = 45)
    plt.yticks(rotation = 45)
    plt.tight_layout()

    plt.show()


