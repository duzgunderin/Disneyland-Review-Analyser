class Review:

    def __init__(self, branch, reviewer_location, rating, year_month):

        self.branch = branch
        self.reviewer_location = reviewer_location
        self.rating = rating
        self.year_month = year_month

    def display_reviewee(self):

        print("Branch: ", self.branch)
        print("Reviewer Location: ", self.reviewer_location)
        print("Rating: ", self.rating)
        print("Year Month: ", self.year_month)

