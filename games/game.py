class Game:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def play(self, balance):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def update_balance(self, amount):
        self.balance += amount
