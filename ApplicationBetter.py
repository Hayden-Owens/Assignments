#Title: Judo Application
#Author: Hayden Owens
#Date: 26/11/2023
#Description: This application is for calculating the monthly fees for North Sussex Judo clients

#Class and attributes
class MonthlyFee:
    def __init__(self):
        self.name = None
        self.weight = None
        self.weight_category = None
        self.training_plan = None
        self.competition = None
        self.private_coaching = None
        self.total_fee = None


    def UserInput(self):
        self.name = input("Enter the athletes full name: ")
        self.weight = float(input("Enter the athletes current weight in (kg): "))
        self.training_plan = input("Enter the athletes training plan. (Beginner, Intermediate, or Elite): ")
        if self.training_plan.lower() == ("beginner"):
            self.private_coaching = input("How many hours of private coaching will the athlete be attending this month?. (Max 20): ")
        else:
            self.competition = input("How many competitions will the athlete enter this month? (0, 1, or 2): ")
            self.private_coaching = input("How many hours of private coaching will the athlete be attending this month?. (Max 20): ")


    def UserResponse(self):
        self.UserInput()
        print(f" - Athletes full name: {self.name}.")
        print(f" - Athletes current weight category is {self.WeightCategory()}.")
        print(f" - Selected training plan £{float(self.TrainingFee())} per month.")
        if self.training_plan.lower() == ("beginner"):
            print(f" - Private Coaching £{self.CoachingFee()} for the month.")
        else:
            print(f" - Competitions £{self.CompetitionFee()} for the month.")
            print(f" - Private Coaching £{self.CoachingFee()} for the month.")
        if self.training_plan.lower() == ("beginner"):
            print(f" - Total monthly fee = £{self.TrainingFee() + self.CoachingFee()}.")
        else:
            print(f" - Total monthly fee = £{self.CoachingFee() + self.TrainingFee() + self.CompetitionFee()}.")

    def WeightCategory(self):
        if 0 <= self.weight <= 66:
            return "flyweight"
        elif 67 <= self.weight <= 73:
            return "lightweight"
        elif 74 <= self.weight <= 81:
            return "light-middleweight"
        elif 82 <= self.weight <= 90:
            return "middleweight"
        elif 91 <= self.weight <= 100:
            return "light-heavyweight"
        else:
            return "heavyweight"

    def TrainingFee(self):
        if self.training_plan.lower() == "beginner":
            return float((25 * 4))
        elif self.training_plan.lower() == "intermediate":
            return float((30 * 4))
        elif self.training_plan.lower() == "elite":
            return float((35 * 4))
        else:
            return 0.0

    def CompetitionFee(self):
        if self.competition == "0":
            return 0
        elif self.competition == "1":
            return 22
        elif self.competition == "2":
            return 44
        else:
            return "ERROR"

    def CoachingFee(self):
        self.week_cost = float(9.50)
        self.priv_answer = float(self.private_coaching) * self.week_cost
        if 1 <= float(self.private_coaching) <= 20:
            return self.priv_answer
        else:
            return float(0)

# Usage
run_application = MonthlyFee()
run_application.UserResponse()
