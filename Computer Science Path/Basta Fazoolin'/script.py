from datetime import datetime


class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = datetime.strptime(start_time, "%I%p")
        self.end_time = datetime.strptime(end_time, "%I%p")

    def __repr__(self):
        formatted_start_time = self.start_time.strftime("%-H%p").lower()
        formatted_end_time = self.end_time.strftime("%-H%p").lower()
        str = "{} menu available from {} to {}".format(
            self.name, formatted_start_time, formatted_end_time)
        return str

    def calculate_bill(self, purchased_items):
        total = 0
        for item in self.items.keys():
            total += self.items.get(item, 0)

        return total


brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,
    'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00, 'espresso': 3.00,
}

kids_items = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}


brunch = Menu("Brunch", brunch_items, "11am", "4pm")
early_bird = Menu("Early bird", early_bird_items, "3pm", "6pm")
dinner = Menu("Dinner", dinner_items, "5pm", "11pm")
kids = Menu("Kids", kids_items, "11am", "9pm")

print(brunch)

brekkie = ["pancakes", "home fries", "coffee"]
print(brunch.calculate_bill(brekkie))

early = ['salumeria plate', 'mushroom ravioli (vegan)']
print(early_bird.calculate_bill(early))


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        str = f"Franchise: {self.address}"
        return str

    def available_menus(self, time):
        time = datetime.strptime(time, "%I%p")
        available = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available.append(menu)
        return available


menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
print(flagship_store)

print(flagship_store.available_menus("5pm"))


class Business:

    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


basta = Business("Basta Fazoolin' with my Heart",
                 franchises=[flagship_store, new_installment])


menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50,
    'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Arepa's Menu", menu, "10am", "8pm")
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
arepa = Business("Take a' Arepa", arepas_place)
