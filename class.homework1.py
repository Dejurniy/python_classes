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

        for key, value in self.dict.items():
            if value > 5:
                print(key)


first_mth = Dict("python", {}, {})
second_mth = Dict("", {"key1": 1, "key2": 2, "key3": 1}, {})
third_mth = Dict("", {"key1": 1, "key2": 2, "key3": 10, "key4": 14, "key5": 18}, {})

Dict.convert(first_mth)
Dict.no_dups(second_mth)
Dict.highest(third_mth)
