import csv

def load_reviews(file_path):

#read the Disneyland review dataset from CSV file and stores each review inside the list.
    reviews = []
#open the CSV file
    with open(file_path, "r", encoding="utf-8") as file:
#read the file
        csv_reader = csv.DictReader(file)
#loop through each row in the dataset
        for row in csv_reader:
#convert rating into integer
            row["Rating"] = int(row["Rating"])
#add row to reviews the list
            reviews.append(row)

    return reviews

#returns all reviews for the selected park
def get_reviews_by_park(reviews, park_name):
    matching_reviews = []

    #loop through all reviews
    for review in reviews:
        print(review["Branch"])
        #check if the branch matches the selected park
        if review["Branch"].lower() == park_name.lower():
            matching_reviews.append(review)

    return matching_reviews

#counts reviews for a park from a specific location
def count_reviews_by_location(reviews, park_name, location):
    review_count = 0

    for review in reviews:
        if (
            review["Branch"].lower() == park_name.lower()
            and
            review["Reviewer_Location"].lower() == location.lower()
        ):
            review_count += 1

    return review_count

#counts how many reviews each park has received.
def count_reviews_per_park(reviews):
    park_counts = {}

    for review in reviews:
        park_name = review["Branch"]

        if park_name not in park_counts:
            park_counts[park_name] = 0

        park_counts [park_name] += 1

    return park_counts

#finds the top 10 reviewer locations with the highest average rating for the selected plan
def get_top_10_locations_by_average_rating(reviews, park_name):
    location_scores ={}

    for review in reviews:
        if review["Branch"].lower() == park_name.lower():
            location = review["Reviewer_Location"]

            if location not in location_scores:
                location_scores[location] = {"total": 0, "count": 0}

            location_scores[location]["total"] += review["Rating"]
            location_scores[location]["count"] += 1
    location_averages = {}

    for location, values in location_scores.items():
        average = values["total"] / values["count"]
        location_averages[location] = round(average, 2)

    top_10_locations = dict(sorted(location_averages.items(), key=lambda item: item[1], reverse=True) [:10])

    return top_10_locations

#calculates the average rating for each month for a selected park.
def get_average_rating_by_month(reviews, park_name):

    month_scores = {}

    for review in reviews:
        branch = review["Branch"].strip().lower()
        selected_park = park_name.strip().lower()

        print(review["Branch"])
        print(review["Year_Month"])

        if branch == selected_park:
            year_month = review["Year_Month"]

            if year_month != "missing":
                month = year_month.split("-")[1]

                if month not in month_scores:
                    month_scores[month] = {"total": 0, "count": 0}

                month_scores[month_scores]["total"] += int(review["Rating"])
                month_scores[month]["count"] += 1

        month_averages = {}

        month_order = [
           "1", "2","3","4","5","6","7","8","9","10","11","12"
        ]



        for month in month_order:
            if month in month_scores:

                total = month_scores[month]["total"]
                count = month_scores[month]["count"]

                month_averages[month] = round(total / count, 2)

        return month_averages
    return None


def export_summary(reviews):


    park_counts = count_reviews_per_park(reviews)

    with open("exported_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Park Name", "Number of Reviews"])

        for park, count in park_counts.items():
            writer.writerow([park, count])

    print("Data exported successfully")

    return reviews
