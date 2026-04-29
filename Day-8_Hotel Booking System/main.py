from matplotlib.style import available


class room:
    def __init__(self,room_number,room_type,price):
        self.room_number = room_number
        self.room_type = room_type
        self.price= price
        self.is_booked = False
    def book(self):
        if self.is_booked:
            print(f"room {self.room_number} already booked")
            return False
        self.is_booked= True
        print(f"the room{self.room_number} is booked")
        return True
    def checkout(self):
        if not self.is_booked:
            print(f"room {self.room_number} not booked")
            return False
        self.is_booked = False
        print(f"room {self.room_number} is available!!")
        return True
    def display(self):
        status = "booked" if self.is_booked else "available"
        print(f" Room: {self.room_number} | {self.room_type}  |  {self.price} | {status} ")

class HOTAL:
    def __init__(self,name):
        self.name = name
        self.rooms=[]
    def add_rooms(self,room):
        self.rooms.append(room)
    def show_available_rooms(self):
        print('\n Available rooms:')
        found =False
        for room in self.rooms:
            if not room.is_booked:
                room.display()
                found =True
        if not found:
            print('no rooms available!!')
    def book_room(self,room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.book()
        print("room no found!")
        return False
    def check_out_room(self,room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.checkout()
        print("room not found")
        return False
hotal  = HOTAL("hiv final boss")
r1 = room(102,"single",2000)
r2 = room(103,"double",5000)
r3 = room(104,"king",10000)

hotal.add_rooms(r1)
hotal.add_rooms(r2)
hotal.add_rooms(r3)

hotal.show_available_rooms()
print()
hotal.book_room(102)
hotal.book_room(103)
hotal.book_room(104)
hotal.book_room(103)

print()
hotal.show_available_rooms()
print()
hotal.check_out_room(102)
hotal.check_out_room(103)
hotal.check_out_room(104)
print()
hotal.show_available_rooms()