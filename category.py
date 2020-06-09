class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        # also a string representation
        return f"self.name = {self.name} ; self.description = {self.description} ; self.products = {self.products}"
