'''
1.	Define a Movie object that can store the data for each movie
a.	Add a module named objects to the program folder
b.	In the object module, write the code for a class  named Movie that 
defines a Movie object that stores the name and year of a movie. 
This class should include a getStr() method that returns the name of the movie 
followed by its year in parentheses.
'''

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def getStr(self):
        return 'Name: {} Year: {}'.format(self.name, self.year)


# m1 = Movie("123", "456")

# print(m1.name)
# print(m1.year)
# print(m1.getStr())

# class Hey:
#     a = 12
#     def __init__(self, b, c):
#         self.b = b
#         self.c = c


# h1 = Hey("Hello", "World")
# print(h1.b)
# print(h1.c)

        