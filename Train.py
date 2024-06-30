class Train:
    def __init__(self, train_no, train_name, Starting, destination):
        # The constructor method initializes the attributes train_no, train_name, Starting, and destination for the Train instance
        self.train_no = train_no
        self.train_name = train_name
        self.Starting = Starting
        self.destination = destination

        # Initialize lists of coaches
        self.sleeper_coaches = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']
        self.ac_coaches = ['B1', 'B2']
        self.first_class_coaches = ['A1']
        self.general_coaches = ['G1', 'G2']

        # Initialize the number of seats in different types of coaches
        self.sleeper_seats = 40
        self.two_tier_seats = 18
        self.first_class_seats = 8
        self.general_seats = 40

    def __str__(self):
        # This method returns a string representation of the Train instance
        return f"Train Number: {self.train_no}\nTrain Name: {self.train_name}\nStarting Station: {self.Starting}\nDestination Station: {self.destination}"

# Demonstration
# Create an instance of the Train class with train number 1234, train name "Express Train", starting station "Mumbai", and destination station "Delhi"
# train = Train(1234, "Express Train", "Mumbai", "Delhi")
# Print the string representation of the Train instance
# print(train)
