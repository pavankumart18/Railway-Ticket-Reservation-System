from Person import Person  # Importing the Person class from Person module
from Train import Train    # Importing the Train class from Train module
import random             # Importing random module for random operations

class Berth:
    def __init__(self, person, train, class_type, seat_type,
                 default_seats_count_class_type, default_seat_count_seats_type,
                 booked_seats, booked_seats_by_seats_type, seats_booked_coach_wise,
                 coaches, waiting_list, seats_count_coach_wise, seats_count_coach_wise_gender):
        # Initializing Berth object with necessary attributes
        self.train = train
        self.person = person
        self.gender = person.gender  # Extracting gender from Person object
        self.seat_type = seat_type
        self.class_type = class_type
        self.seat = None           # Initializing seat variable
        self.coach = None          # Initializing coach variable
        self.final_seat_type = None  # Initializing final seat type variable

        # Mapping seat categories for each class type
        self.actual_order = {
            "First Class": ["Lower Berth"],
            "AC": ["Upper Berth", "Lower Berth"],
            "Sleeper": ["Upper Berth", "Middle Berth", "Lower Berth"]
        }

        # Setting default seat counts and booked seats information
        self.default_seats_count_class_type = default_seats_count_class_type
        self.default_seat_count_seats_type = default_seat_count_seats_type
        self.booked_seats = booked_seats
        self.booked_seats_by_seats_type = booked_seats_by_seats_type
        self.seats_booked_coach_wise = seats_booked_coach_wise
        self.seats_count_coach_wise = seats_count_coach_wise
        self.seats_count_coach_wise_gender = seats_count_coach_wise_gender

        # Extracting coach information based on class type
        self.sleeper_coaches = coaches["Sleeper"]
        self.ac_coaches = coaches["AC"]
        self.first_class_coaches = coaches["First Class"]
        self.general_coaches = coaches["General"]

        # Initializing waiting list
        self.waiting_list = waiting_list

    # Method to determine berth category based on age
    def find_category(self, age):
        if age >= 60:
            return "Lower Berth"
        elif age >= 20:
            return "Middle Berth"
        else:
            return "Upper Berth"

    # Method to select a seat based on priority
    def seat_selection1(self, priority):
        coach = None
        seat = None
        final_seat_type = None

        # First Class seat selection logic
        if self.class_type == "First Class" and len(self.booked_seats[self.class_type]) < self.default_seats_count_class_type[self.class_type]:
            coaches = self.train.first_class_coaches
            random.shuffle(coaches)
            for seat_t in priority:
                if len(self.booked_seats_by_seats_type[seat_t]) < self.default_seat_count_seats_type[self.class_type][seat_t]:
                    for coach in coaches:
                        if (len(self.seats_count_coach_wise[coach]) < len(self.train.first_class_coaches) * (self.train.first_class_seats)
                                and len(self.seats_booked_coach_wise[coach][seat_t]) < self.default_seat_count_seats_type[self.class_type][seat_t] // len(self.train.first_class_coaches)):
                            while True:
                                seat = random.randint(1, self.train.first_class_seats)
                                if seat not in self.seats_booked_coach_wise[coach][seat_t]:
                                    # Gender-specific seat allocation logic
                                    if self.gender == "Female":
                                        if seat % 2 == 1:
                                            if seat + 1 in self.seats_count_coach_wise_gender[coach] and self.seats_count_coach_wise_gender[coach][seat + 1] != "Male":
                                                final_seat_type = seat_t
                                                break
                                            elif seat + 1 not in self.seats_count_coach_wise_gender[coach]:
                                                final_seat_type = seat_t
                                                break
                                            else:
                                                final_seat_type = seat_t
                                                break
                                        elif seat % 2 == 0:
                                            if seat - 1 in self.seats_count_coach_wise_gender[coach] and self.seats_count_coach_wise_gender[coach][seat - 1] != "Male":
                                                final_seat_type = seat_t
                                                break
                                            elif seat - 1 not in self.seats_count_coach_wise_gender[coach]:
                                                final_seat_type = seat_t
                                                break
                                            else:
                                                final_seat_type = seat_t
                                                break
                                    elif self.gender == "Male":
                                        final_seat_type = seat_t
                                        break
                        if final_seat_type is not None:
                            break
                if final_seat_type is not None:
                    break

        # AC class seat selection logic
        elif self.class_type == "AC" and len(self.booked_seats[self.class_type]) < self.default_seats_count_class_type[self.class_type]:
            coaches = self.train.ac_coaches
            random.shuffle(coaches)
            for seat_t in priority:
                if len(self.booked_seats_by_seats_type[seat_t]) < self.default_seat_count_seats_type[self.class_type][seat_t]:
                    for coach in coaches:
                        if len(self.seats_count_coach_wise[coach]) < len(self.train.ac_coaches) * (self.train.two_tier_seats) \
                                and len(self.seats_booked_coach_wise[coach][seat_t]) < self.default_seat_count_seats_type[self.class_type][seat_t] // len(self.train.ac_coaches):
                            while True:
                                seat = random.randint(1, self.train.two_tier_seats)
                                if seat not in self.seats_booked_coach_wise[coach][seat_t]:
                                    # Gender-specific seat allocation logic for AC coaches
                                    if seat_t == "Upper Berth":
                                        if seat % 3 == 2:
                                            if self.gender == "Female":
                                                if seat - 1 in self.seats_count_coach_wise_gender[coach] and self.seats_count_coach_wise_gender[coach][seat - 1] != "Male":
                                                    final_seat_type = seat_t
                                                    break
                                                elif seat - 1 not in self.seats_count_coach_wise_gender[coach]:
                                                    final_seat_type = seat_t
                                                    break
                                                else:
                                                    final_seat_type = seat_t
                                                    break
                                            elif self.gender == "Male":
                                                final_seat_type = seat_t
                                                break
                                        elif seat % 3 == 0 and seat % 6 != 0:
                                            if self.gender == "Female":
                                                if seat + 3 < self.train.two_tier_seats and seat + 3 in self.seats_count_coach_wise_gender[coach] and self.seats_count_coach_wise_gender[coach][seat + 3] != "Male":
                                                    final_seat_type = seat_t
                                                    break
                                                elif seat + 3 < self.train.two_tier_seats and seat + 3 not in self.seats_count_coach_wise_gender[coach]:
                                                    final_seat_type = seat_t
                                                    break
                                                else:
                                                    final_seat_type = seat_t
                                                    break
                                            elif self.gender == "Male":
                                                final_seat_type = seat_t
                                                break
                                    elif seat_t == "Lower Berth":
                                        if seat % 3 == 1:
                                            if self.gender == "Female":
                                                if seat + 1 in self.seats_count_coach_wise_gender[coach] and self.seats_count_coach_wise_gender[coach][seat + 1] != "Male":
                                                    final_seat_type = seat_t
                                                    break
                                                elif seat + 1 not in self.seats_count_coach_wise_gender[coach]:
                                                    final_seat_type = seat_t
                                                    break
                                                else:
                                                    final_seat_type = seat_t
                                                    break
                                            elif self.gender == "Male":
                                                final_seat_type = seat_t
                                                break
                                        elif (seat % 6 == 0):
                                            if self.gender == "Female":
                                                if seat - 3 > 0 and seat - 3 in self.seats_count_coach_wise_gender[coach] and self.seats_count_coach_wise_gender[coach][seat - 3] != "Male":
                                                    final_seat_type = seat_t
                                                    break
                                                elif seat - 3 > 0 and seat - 3 not in self.seats_count_coach_wise_gender[coach]:
                                                    final_seat_type = seat_t
                                                    break
                                                else:
                                                    final_seat_type = seat_t
                                                    break
                                            elif self.gender == "Male":
                                                final_seat_type = seat_t
                                                break
                            if final_seat_type is not None:
                                break
                    if final_seat_type is not None:
                        break

        # Sleeper class seat selection logic
        elif self.class_type == "Sleeper" and len(self.booked_seats[self.class_type]) < self.default_seats_count_class_type[self.class_type]:
            coaches = self.train.sleeper_coaches
            random.shuffle(coaches)
            for seat_t in priority:
                if len(self.booked_seats_by_seats_type[seat_t]) < self.default_seat_count_seats_type[self.class_type][seat_t]:
                    for coach in coaches:
                        if len(self.seats_count_coach_wise[coach]) < len(self.train.sleeper_coaches) * (self.train.sleeper_seats) \
                                and len(self.seats_booked_coach_wise[coach][seat_t]) < self.default_seat_count_seats_type[self.class_type][seat_t] // len(self.train.sleeper_coaches):
                            while True:
                                seat = random.randint(1, self.train.sleeper_seats)
                                if seat not in self.seats_booked_coach_wise[coach][seat_t]:
                                    # Gender-specific seat allocation logic for Sleeper coaches
                                    if seat_t == "Upper Berth":
                                        if seat % 4 == 3:
                                            if self.gender == "Female":
                                                if seat - 1 in self.seats_count_coach_wise_gender[coach] and self.seats_count_coach_wise_gender[coach][seat - 1] != "Male":
                                                    final_seat_type = seat_t
                                                    break
                                                elif seat - 1 not in self.seats_count_coach_wise_gender[coach]:
                                                    final_seat_type = seat_t
                                                    break
                                                else:
                                                    final_seat_type = seat_t
                                                    break
                                            elif self.gender == "Male":
                                                final_seat_type = seat_t
                                                break
                                        elif seat % 4 == 1 and seat % 8 != 0:
                                            if self.gender == "Female":
                                                if seat + 4 < self.train.sleeper_seats and seat + 4 in self.seats_count_coach_wise_gender[coach] and \
                                                        self.seats_count_coach_wise_gender[coach][seat + 4] != "Male":
                                                    final_seat_type = seat_t
                                                    break
                                                elif seat + 4 < self.train.sleeper_seats and seat + 4 not in self.seats_count_coach_wise_gender[coach]:
                                                    final_seat_type = seat_t
                                                    break
                                                else:
                                                    final_seat_type = seat_t
                                                    break
                                            elif self.gender == "Male":
                                                final_seat_type = seat_t
                                                break
                                    elif seat_t == "Middle Berth" and seat % 4 == 2:
                                        if self.gender == "Female":
                                            if seat - 1 in self.seats_count_coach_wise_gender[coach] and \
                                                    self.seats_count_coach_wise_gender[coach][seat - 1] != "Male" and seat + 1 in self.seats_count_coach_wise_gender[coach] and self.seats_count_coach_wise_gender[coach][seat + 1] != "Male":
                                                final_seat_type = seat_t
                                                break
                                            elif seat - 1 not in self.seats_count_coach_wise_gender[coach] or seat + 1 not in self.seats_count_coach_wise_gender[coach]:
                                                final_seat_type = seat_t
                                                break
                                            else:
                                                final_seat_type = seat_t
                                                break
                                        elif self.gender == "Male":
                                            final_seat_type = seat_t
                                            break
                                    elif seat_t == "Lower Berth":
                                        if seat % 4 == 1:
                                            if self.gender == "Female":
                                                if seat + 1 in self.seats_count_coach_wise_gender[coach] and self.seats_count_coach_wise_gender[coach][seat + 1] != "Male":
                                                    final_seat_type = seat_t
                                                    break
                                                elif seat + 1 not in self.seats_count_coach_wise_gender[coach]:
                                                    final_seat_type = seat_t
                                                    break
                                                else:
                                                    final_seat_type = seat_t
                                                    break
                                            elif self.gender == "Male":
                                                final_seat_type = seat_t
                                                break
                                        elif seat % 8 == 0:
                                            if self.gender == "Female":
                                                if seat - 4 > 0 and seat - 4 in self.seats_count_coach_wise_gender[coach] and self.seats_count_coach_wise_gender[coach][seat - 4] != "Male":
                                                    final_seat_type = seat_t
                                                    break
                                                elif seat - 4 > 0 and seat - 4 not in self.seats_count_coach_wise_gender[coach]:
                                                    final_seat_type = seat_t
                                                    break
                                                else:
                                                    final_seat_type = seat_t
                                                    break
                                            elif self.gender == "Male":
                                                final_seat_type = seat_t
                                                break
                            if final_seat_type is not None:
                                break
                    if final_seat_type is not None:
                        break

        # If seat selection fails, return None
        if seat == None and final_seat_type == None:
            return

        # Assigning selected seat and coach to object attributes
        self.seat = seat
        self.coach = coach
        self.final_seat_type = final_seat_type
        return

    # Method to determine seat number
    def seat_no(self):
        # General class seat selection logic
        if self.class_type == "General":
            coaches = self.train.general_coaches
            random.shuffle(coaches)
            for coach in coaches:
                if len(self.seats_count_coach_wise[coach]) < len(self.train.general_coaches) * (
                        self.train.general_seats):
                    while True:
                        self.seat = random.randint(1, self.train.general_seats)
                        if self.seat not in self.seats_booked_coach_wise[coach]:
                            self.coach = coach
                            break
                    if self.coach is not None:
                        break
            return self.seat, None, self.coach

        # For other class types, determine seat priority
        seat_t = self.seat_type
        preferred_by_algo = self.find_category(self.person.age)
        priority = []

        # Determine seat priority based on class type
        if self.class_type == "First Class":
            order = self.actual_order[self.class_type]
            priority += order
        elif self.class_type == "AC":
            order = self.actual_order[self.class_type]
            if preferred_by_algo == "Middle Berth":
                preferred_by_algo = "Lower Berth"
            if seat_t == preferred_by_algo:
                priority.append(seat_t)
                order.remove(seat_t)
                priority += order
            elif seat_t != preferred_by_algo:
                priority.append(preferred_by_algo)
                priority.append(seat_t)
                order.remove(preferred_by_algo)
                order.remove(seat_t)
                priority += order
        else:
            order = self.actual_order[self.class_type]
            if seat_t == preferred_by_algo:
                priority.append(seat_t)
                order.remove(seat_t)
                priority += order
            elif seat_t != preferred_by_algo:
                priority.append(preferred_by_algo)
                priority.append(seat_t)
                order.remove(preferred_by_algo)
                order.remove(seat_t)
                priority += order

        # Call seat selection method based on determined priority
        self.seat_selection1(priority)

    # Method to find and return the seat, seat type, and coach
    def find_seat(self):
        self.seat_no()
        return self.seat, self.final_seat_type, self.coach
