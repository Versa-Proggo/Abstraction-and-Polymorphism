class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh")
    def language(self):
        print("Bangla is 1 of the State Laguage of BANGLADESH")
    def type(self):
        print("Bangladesh is a developing country")
class United_States_of_America():
    def capital(self):
        print("Washington D.C. is the capital of United States of America")
    def language(self):
        print("English Laguage of United States of America")
    def type(self):
        print("United States of America is a developed country")
b = Bangladesh()
u = United_States_of_America()
for country in (b,u):
    country.capital()
    country.language()
    country.type()