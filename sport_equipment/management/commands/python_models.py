class Category:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        return f'{self.name} {self.rating}'


class CategoryCard:

    def __init__(self, category, text):
        self.category = category
        self.text = text

    def __str__(self):
        return f'{self.category} {self.text}'


class Tag:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Equipment:

    def __init__(self, name, category, tags):
        self.name = name
        self.category = category
        self.tags = tags

    def __str__(self):
        return self.name
