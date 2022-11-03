class Dict:

    def __init__(self, string, dict, dict_2):
        self.string = string
        self.dict = dict
        self.dict_2 = dict_2

    # First method
    def convert(self):

        """
        This method creates dictionary from a given string
        """

        for cr in self.string:
            if cr not in self.dict:
                self.dict[cr] = 1

        print(self.dict)

    # Second method
    def no_dups(self):

        """
        This method returns dictionary without duplicates
        """

        for key, value in self.dict.items():
            if value not in self.dict_2.values():
                self.dict_2[key] = value

        print(self.dict_2)

    def highest(self):

        """
        This method returns the highest 3 values in a dictionary!
        """
        max_ = 0

        for key, value in self.dict.items():
            if max_ < value:
                max_ = value
                print(max_)


first_mth = Dict("python", {}, {})
second_mth = Dict("", {"key1": 1, "key2": 2, "key3": 1}, {})
third_mth = Dict("", {"key1": 1, "key2": 2, "key3": 10, "key4": 14, "key5": 18}, {})

Dict.convert(first_mth)
Dict.no_dups(second_mth)
Dict.highest(third_mth)


class Circle:

    def __init__(self, P, r):
        self.P = P
        self.r = r

    def circle_area(self):
        """
        This method computes the area of the circle!
        """

        return self.P * self.r ** 2

    def circle_perimeter_(self):
        """
        This method computes the perimeter of circle!
        """

        return 2 * self.P * self.r


circle = Circle(3.14, 7)
print("The area of the circle is:", Circle.circle_area(circle))
print("The perimeter of the circle is:", Circle.circle_perimeter_(circle))
