# Train Reservation Booking System - Based on Gender

This project implements a train berth booking system in Python. It allows for booking train berths across different classes and seat types, while also providing visual representations of each class's seating arrangement.

## Features

- **Berth Booking**: Book train berths based on class type, seat type, and passenger details.
- **Seat Allocation**: Automatically allocate seats based on passenger preferences and availability.
- **Visual Representation**: Display visual layouts of train compartments for different classes (Sleeper, AC, First Class, General).

## Classes Implemented

1. **Berth Class (`Berth`)**:
   - Manages the booking and allocation of train berths.
   - Utilizes various algorithms to allocate seats based on passenger preferences.

2. **Train Classes (`Sleeper`, `AC`, `FirstClass`, `General`)**:
   - Each class represents a different type of train compartment.
   - Provides methods to visually display the seating arrangement within the compartment.

## Usage

To use the system:
1. Import the necessary classes (`Berth`, `Sleeper`, `AC`, `FirstClass`, `General`) from their respective modules.
2. Initialize a `Berth` object with passenger details and desired train class.
3. Use the `find_seat` method to allocate a seat.
4. Optionally, use the draw methods of individual train classes to visualize seating arrangements.

## Installation
git clone https://github.com/your-username/train-berth-booking.git
cd train-berth-booking
python main.py

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to submit a pull request.


### Notes:
- Replace `pavankumat18` with your GitHub username in the clone URL.
- Ensure you have a `LICENSE` file in your repository if you choose to use the MIT License mentioned in the `README.md`.

This `README.md` file provides an overview of your project, its features, usage instructions, and details on how others can contribute to it. Adjust the content as per your project structure and requirements before publishing on GitHub.
