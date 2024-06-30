#Sleeper class
class Sleeper:
    def __init__(self, width=3, height=3, no=40,seat_booked=[]):
        self.width = width
        self.height = height
        self.no = list(range(1, no + 1))
        self.reserved_seats = seat_booked

    def draw_box(self):
        for e in range(4):
            l = e
            if e == 3:
                print("-------" * 13)

            for i in range(self.height):
                for j in range(self.width * 10):
                    if j != 0 and j % 3 == 0:
                        print("  ", end="")
                    if j%6==0:
                        print("| ",end="")

                    if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                        if i != 0 and i != self.height - 1:
                            print("| ", end="")
                        else:
                            print("- ", end="")
                    elif j % self.width == 0 or j % self.width == 2:
                        print("| ", end="")
                    elif i == self.height // 2 and j % self.width == 1:
                        if self.no[l] not in self.reserved_seats:
                            if l < 9:
                                print(f'{self.no[l]} ', end="")
                                l += 4
                            else:
                                print(f'{self.no[l]}', end="")
                                l += 4
                        else:
                            l += 4
                            print('R ', end="")
                    else:
                        print(' ', end="")
                print()
            print()
#AC
class AC:
    def __init__(self, width=3, height=3, no=18,seat_booked=[]):
        self.width = width
        self.height = height
        self.no = list(range(1, no + 1))
        self.reserved_seats = seat_booked

    def draw_box(self):
        for e in range(3):
            l = e
            if e == 2:
                print("----------" * 5)

            for i in range(self.height):
                for j in range(self.width * 6):
                    if j != 0 and j % 3 == 0:
                        print("  ", end="")
                    if j%6==0:
                        print("| ", end="")

                    if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                        if i != 0 and i != self.height - 1:
                            print("| ", end="")
                        else:
                            print("- ", end="")
                    elif j % self.width == 0 or j % self.width == 2:
                        print("| ", end="")
                    elif i == self.height // 2 and j % self.width == 1:
                        if self.no[l] not in self.reserved_seats:
                            if l < 9:
                                print(f'{self.no[l]} ', end="")
                                l += 3
                            else:
                                print(f'{self.no[l]}', end="")
                                l += 3
                        else:
                            l += 3
                            print('R ', end="")
                    else:
                        print(' ', end="")
                print()
            print()

#First Class
class FirstClass:
    def __init__(self, width=3, height=3, no=8,seat_booked=[]):
        self.width = width
        self.height = height
        self.no = list(range(1, no + 1))
        self.reserved_seats = seat_booked

    def draw_box(self):
        for e in range(1):
            l = e
            if e == 2:
                print("-------" * 9)

            for i in range(self.height):
                for j in range(self.width * 8):
                    if j != 0 and j % 3 == 0:
                        print("  ", end="")
                    if j%6==0:
                        print("| ", end="")

                    if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                        if i != 0 and i != self.height - 1:
                            print("| ", end="")
                        else:
                            print("- ", end="")
                    elif j % self.width == 0 or j % self.width == 2:
                        print("| ", end="")
                    elif i == self.height // 2 and j % self.width == 1:
                        if self.no[l] not in self.reserved_seats:
                            if l < 9:
                                print(f'{self.no[l]} ', end="")
                                l += 1
                            else:
                                print(f'{self.no[l]}', end="")
                                l += 1
                        else:
                            l += 1
                            print('R ', end="")
                    else:
                        print(' ', end="")
                print()
            print()
#Sleeper class
class General:
    def __init__(self, width=3, height=3, no=40,seat_booked=[]):
        self.width = width
        self.height = height
        self.no = list(range(1, no + 1))
        self.reserved_seats = seat_booked

    def draw_box(self):
        for e in range(4):
            l = e
            if e == 3:
                print("-------" * 13)

            for i in range(self.height):
                for j in range(self.width * 10):
                    if j != 0 and j % 3 == 0:
                        print("  ", end="")
                    if j%6==0:
                        print("| ",end="")

                    if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                        if i != 0 and i != self.height - 1:
                            print("| ", end="")
                        else:
                            print("- ", end="")
                    elif j % self.width == 0 or j % self.width == 2:
                        print("| ", end="")
                    elif i == self.height // 2 and j % self.width == 1:
                        if self.no[l] not in self.reserved_seats:
                            if l < 9:
                                print(f'{self.no[l]} ', end="")
                                l += 4
                            else:
                                print(f'{self.no[l]}', end="")
                                l += 4
                        else:
                            l += 4
                            print('R ', end="")
                    else:
                        print(' ', end="")
                print()
            print()
#Testing
# b=BoxC()
# b.draw_box()
#Testing
# b=BoxB()
# b.draw_box()
#Testing
# b=BoxA()
# b.draw_box()