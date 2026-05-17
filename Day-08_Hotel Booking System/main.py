class Room:
    def __init__(self,room_number,room_type,price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def book(self):
        if self.is_booked:
            print(f"Room {self.room_number} is already booked")
            return False
        self.is_booked = True
        print(f" Room {self.room_number} is booked!")
        return True
    def checkout(self):
        if not self.is_booked:
            print(f"Room {self.room_number} is not booked")
            return False
        self.is_booked = False
        print(f" Room {self.room_number} is checked out and  available for booking!")
        return True
    def display(self):
        status = "Booked" if self.is_booked else "Available"
        print(f"Room number: {self.room_number} | Room type: {self.room_type} | Room price: {self.price} | Avilability: {status}")

class Hotal:
    def __init__(self,name):
        self.name = name
        self.rooms = []
    def add_room(self,room):
        self.rooms.append(room)
    def show_available_rooms(self):
        print("Available rooms: ")
        found =False
        for room in self.rooms:
            if not room.is_booked:
                room.display()
                found=True
        if not found:
            print("No rooms available!")
    def book_room(self,room_number):
        for room in self.rooms:
            if  room.room_number ==room_number:
                return room.book()
        print("Room number not found")
        return False
    def checkout_room(self,room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.checkout()
        print("Room number not found")
        return False
    
hotal  = Hotal("hiv final boss")
r1 = Room(102,"single",2000)
r2 = Room(103,"double",5000)
r3 = Room(104,"king",10000)

hotal.add_room(r1)
hotal.add_room(r2)
hotal.add_room(r3)

hotal.show_available_rooms()
print()
hotal.book_room(102)
hotal.book_room(103)
hotal.book_room(104)
hotal.book_room(103)

print()
hotal.show_available_rooms()
print()
hotal.checkout_room(102)
hotal.checkout_room(103)
hotal.checkout_room(104)
print()
hotal.show_available_rooms()
                