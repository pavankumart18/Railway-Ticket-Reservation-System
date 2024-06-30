from Train import Train
from Person import Person
from berth_allotment import Berth
from Grid import Sleeper, AC, FirstClass, General

# Default seat counts by class type and seat type
default_seats_count_class_type = {
    "First Class": 8,
    "AC": 36,
    "Sleeper": 400,
    "General": 80
}

default_seat_count_seats_type = {
    "Sleeper": {
        "Upper Berth": 150,
        "Middle Berth": 100,
        "Lower Berth": 150
    },
    "AC": {
        "Upper Berth": 18,
        "Lower Berth": 18
    },
    "First Class": {
        "Lower Berth": 8
    },
    "General": 80
}

# Track booked seats by class type and seat type
booked_seats = {
    "First Class": [],
    "AC": [],
    "Sleeper": [],
    "General": []
}

booked_seats_by_seats_type = {
    "Upper Berth": [],
    "Middle Berth": [],
    "Lower Berth": []
}

# Track seats booked coach-wise and by gender
seats_booked_coach_wise = {
    "S1": {"Upper Berth": [], "Middle Berth": [], "Lower Berth": []},
    "S2": {"Upper Berth": [], "Middle Berth": [], "Lower Berth": []},
    "S3": {"Upper Berth": [], "Middle Berth": [], "Lower Berth": []},
    "S4": {"Upper Berth": [], "Middle Berth": [], "Lower Berth": []},
    "S5": {"Upper Berth": [], "Middle Berth": [], "Lower Berth": []},
    "S6": {"Upper Berth": [], "Middle Berth": [], "Lower Berth": []},
    "S7": {"Upper Berth": [], "Middle Berth": [], "Lower Berth": []},
    "S8": {"Upper Berth": [], "Middle Berth": [], "Lower Berth": []},
    "S9": {"Upper Berth": [], "Middle Berth": [], "Lower Berth": []},
    "S10": {"Upper Berth": [], "Middle Berth": [], "Lower Berth": []},
    "B1": {"Upper Berth": [], "Lower Berth": []},
    "B2": {"Upper Berth": [], "Lower Berth": []},
    "A1": {"Lower Berth": []},
    "G1": [],
    "G2": []
}

seats_count_coach_wise = {
    "S1": [], "S2": [], "S3": [], "S4": [], "S5": [],
    "S6": [], "S7": [], "S8": [], "S9": [], "S10": [],
    "B1": [], "B2": [], "A1": [], "G1": [], "G2": []
}

seats_count_coach_wise_gender = {
    "S1": {}, "S2": {}, "S3": {}, "S4": {}, "S5": {},
    "S6": {}, "S7": {}, "S8": {}, "S9": {}, "S10": {},
    "B1": {}, "B2": {}, "A1": {}, "G1": {}, "G2": {}
}

waiting_list = []

class Reservation:
    def __init__(self, train):
        # Initialize the Reservation with the given Train instance
        self.train = train
        self.class_type = ["First Class", "AC", "Sleeper", "General"]
        self.seat_type = ["Upper Berth", "Middle Berth", "Lower Berth"]

        # Collect user information
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: Male Or Female Or Other\n")

        # Initialize reservation data structures
        self.default_seats_count_class_type = default_seats_count_class_type
        self.default_seat_count_seats_type = default_seat_count_seats_type
        self.booked_seats = booked_seats
        self.booked_seats_by_seats_type = booked_seats_by_seats_type
        self.seats_booked_coach_wise = seats_booked_coach_wise

        # Create a Person instance
        self.person = Person(self.name, self.age, self.gender)

        # Initialize coach information
        self.coaches = {
            "Sleeper": train.sleeper_coaches,
            "AC": train.ac_coaches,
            "First Class": train.first_class_coaches,
            "General": train.general_coaches
        }

        # Display and select class type
        for i in range(len(self.class_type)):
            print(f"{i + 1} : {self.class_type[i]}")
        self.select_class = int(input("Enter the corresponding number to class type: "))

        # Adjust seat types based on selected class
        if self.class_type[self.select_class - 1] == "AC":
            self.seat_type.remove("Middle Berth")
        elif self.class_type[self.select_class - 1] == "First Class":
            self.seat_type.remove("Upper Berth")
            self.seat_type.remove("Middle Berth")

        # Book seat based on class type and seat type
        if self.class_type[self.select_class - 1] == "General":
            self.b = Berth(self.person, self.train, self.class_type[self.select_class - 1], None, default_seats_count_class_type, default_seat_count_seats_type, booked_seats, booked_seats_by_seats_type, seats_booked_coach_wise, self.coaches, waiting_list, seats_count_coach_wise, seats_count_coach_wise_gender)
        else:
            for i in range(len(self.seat_type)):
                print(f"{i + 1} : {self.seat_type[i]}")
            self.select_seat = int(input("Enter the corresponding number to seat type: "))
            self.b = Berth(self.person, self.train, self.class_type[self.select_class - 1], self.seat_type[self.select_seat - 1], default_seats_count_class_type, default_seat_count_seats_type, booked_seats, booked_seats_by_seats_type, seats_booked_coach_wise, self.coaches, waiting_list, seats_count_coach_wise, seats_count_coach_wise_gender)

        # Find seat and handle booking results
        self.seat = self.b.find_seat()
        if self.seat[0] == None:
            waiting_list.append(self.person)
            print(waiting_list)
            print("Sorry for your inconvenience, we cannot provide you a seat right now. Hope you understand. Thank you.")
        if self.seat[0] != None and self.class_type[self.select_class - 1] != "General" and self.seat_type[self.select_seat - 1] != self.b.seat_type:
            print(f"Sorry for your inconvenience, we cannot provide you {self.seat_type[self.select_seat - 1]}, but our team found {self.b.seat_type}. Hope you understand. Thank you.")

        self.final_seat_type = self.b.final_seat_type
        if self.seat[0] != None:
            self.booked_seats[self.class_type[self.select_class - 1]].append(self.seat[0])
            if self.class_type[self.select_class - 1] != "General":
                self.booked_seats_by_seats_type[self.final_seat_type].append(self.seat[0])
                self.seats_booked_coach_wise[self.seat[2]][self.final_seat_type].append(self.seat[0])
                seats_count_coach_wise[self.seat[2]].append(self.seat[0])
                seats_count_coach_wise_gender[self.seat[2]][self.seat[0]] = self.gender
                print(self.booked_seats_by_seats_type)
                print(self.booked_seats)
                print(self.seats_booked_coach_wise)
                print(seats_count_coach_wise)
                if self.class_type[self.select_class - 1] == "Sleeper":
                    s = Sleeper(seat_booked=[self.seat[0]])
                    s.draw_box()
                elif self.class_type[self.select_class - 1] == "AC":
                    a = AC(seat_booked=[self.seat[0]])
                    a.draw_box()
                elif self.class_type[self.select_class - 1] == "First Class":
                    f = FirstClass(seat_booked=[self.seat[0]])
                    f.draw_box()
            elif self.class_type[self.select_class - 1] == "General":
                self.seats_booked_coach_wise[self.seat[2]].append(self.seat[0])
                seats_count_coach_wise[self.seat[2]].append(self.seat[0])
                self.booked_seats[self.class_type[self.select_class - 1]].append(self.seat[0])
                seats_count_coach_wise_gender[self.seat[2]][self.seat[0]] = self.gender
                print(self.booked_seats)
                print(self.seats_booked_coach_wise)
                print(seats_count_coach_wise)
                g = General(seat_booked=[self.seat[0]])
                g.draw_box()

    def __str__(self):
        # Return the reservation details if a seat was found, otherwise apologize
        if self.seat[0] != None:
            return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nClass: {self.class_type[self.select_class - 1]}\nSeat Type: {self.final_seat_type}\nCoach: {self.seat[2]}\nSeat No: {self.seat[0]}"
        return "We are extremely sorry"

def main():
    # Main loop to handle multiple reservations
    while True:
        choice = input("Do you want to reserve another seat? (y/n): ")
        if choice.lower() == "y":
            reservation = Reservation(Train(123, "Chennai Express", "Mumbai", "Chennai"))
            print(reservation)
        else:
            break

if __name__ == "__main__":
    main()
