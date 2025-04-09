from heap_based_priority_queue import Priority


class Hotel:
    def __init__(self):
        self.rooms = Priority()

    def add_room(self, room_number, priority):
        self.rooms.insert(room_number, priority)

    def remove_room(self):
        return self.rooms.remove_max()

    def find_room(self, room_number):
        for room in self.rooms.view():
            if room[0] == room_number:
                return room
        return None

    def view_rooms(self):
        return self.rooms.view()


hotel = Hotel()
hotel.add_room(10, 5)
hotel.add_room(15, 4)
hotel.add_room(20, 3)

print("Номери готелю :", hotel.view_rooms())
room, priority = hotel.remove_room()
print(f"Видалено номер {room} з пріоритетом {priority}")
print("Новий список номерів", hotel.view_rooms())
room_to_find = int(input("Введіть номер кімнати"))
found_room = hotel.find_room(room_to_find)
if found_room:
    print(f"номер {found_room[0]} знайдено , з пріорітетом {found_room[1]}")
else:
    print(f"Номер {found_room} , не знайдено")


