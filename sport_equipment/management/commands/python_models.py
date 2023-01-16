class Category:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        return f'{self.name} {self.rating}'