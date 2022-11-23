# Ex. 1
class Country:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent

    def present(self):
        return f"The brand's country is {self.name}, which is located in {self.continent}."


class Brand:
    def __init__(self, brand, date):
        self.brand = brand
        self.date = date

    def present(self):
        return f"So the brand is {self.brand} and it's founded in {self.date}"


class Season:
    def __init__(self, season):
        self.season = season

    def present(self):
        return f"This brand is {self.season} clothing brand!"


class Product(Country, Brand, Season):
    def __init__(self, pr_name, pr_type, pr_price, pr_quantity, percent, *args, **kwargs):
        self.product = pr_name
        self.type = pr_type
        self.price = pr_price
        self.quantity = pr_quantity
        self.percent = percent
        super().__init__(*args, **kwargs)

    def discount(self):
        return self.price - (self.price * self.percent) / 100

    def present(self):
        return f"The product name is {self.product} which type is {self.type}. The price of the product is {self.price}$. " \
               f"{self.quantity} shoes are left! " \
               f"If you want a discount we can offer {self.percent}%." \
               f"It would be from {self.price}$ to {self.discount()}$ "


cn = Country("France", "Europe")
br = Brand("Balenciaga", 1919)
se = Season("all seasons")
pr = Product("Triple S Trainers", "Sneakers", 450, 32, 10, "", "")

print(Country.present(cn))
print(Brand.present(br))
print(Season.present(se))
print(Product.present(pr))


# Ex. 2

class Hotel:
    def __init__(self, hotel_name, place, mid_price, lux_price, *args, **kwargs):
        self.name = hotel_name
        self.place = place
        self.rooms_mid = {"room1": "busy", "room2": "free"}
        self.rooms_mid_price = mid_price
        self.rooms_lux = {"room1": "free", "room2": "busy"}
        self.rooms_lux_price = lux_price
        super().__init__(*args, **kwargs)

    def present(self):
        return f"Welcome to the most luxurious hotel of the city, {self.name}, {self.place}. " \
               f"Of course we have middle rooms and lux rooms. " \
               f"So the price of mid rooms is {self.rooms_mid_price}$ and for lux rooms is {self.rooms_lux_price}$ "

    def discount(self):
        return f"We have a discount for new customers. it would be 10%. " \
               f"So the new price for the mid room is {self.rooms_mid_price - (self.rooms_mid_price * 10) / 100}$. " \
               f"And for the lux room is {self.rooms_lux_price - (self.rooms_lux_price * 10) / 100}$"

    def available_rooms(self):
        return "Available rooms are room2 from mid_rooms and room1 from lux_rooms!"

    def booking_mid(self):
        check = True
        while check:
            for key, value in self.rooms_mid.items():
                if value == "free":
                    return f"You booked {key} of mid_rooms. "

    def booking_lux(self):
        check = True
        while check:
            for key, value in self.rooms_lux.items():
                if value == "free":
                    return f"You booked {key} of lux_rooms. "


class Taxi:
    def __init__(self, taxi_name, car_type, price, *args, **kwargs):
        self.taxi_name = taxi_name
        self.car = car_type
        self.taxi_price = price
        super().__init__(*args, **kwargs)

    def present(self):
        return f"Our taxi service, {self.taxi_name}, offers you cars from {self.car}. " \
               f"It would cost for you just {self.taxi_price} "


class Tour(Hotel, Taxi):
    def __init__(self, tour_name, price_lux, price_mid, *args, **kwargs):
        self.tour_name = tour_name
        self.price_lux = price_lux
        self.price_mid = price_mid
        super().__init__(*args, **kwargs)

    def for_mid(self):
        self.price_mid = self.rooms_mid_price + self.taxi_price
        return self.price_mid

    def for_lux(self):
        self.price_lux = self.rooms_lux_price + self.taxi_price
        return self.price_lux

    def present(self):
        return f"{Hotel.present(self)}\n {Hotel.discount(self)}\n {Hotel.available_rooms(self)}\n {Hotel.booking_lux(self)}\n " \
               f"{Taxi.present(self)}\n " \
               f"So for all lux staff the price is {self.for_lux()}$ and for mid is {self.for_mid()}$"


all = Tour(tour_name="Doggo", price_lux="", price_mid="", hotel_name="Bulgar Al Arab", place="Dubai", mid_price=5000,
           lux_price=10000, taxi_name="DownTown Cab", car_type="Mercedes", price=500)

print(all.present())
