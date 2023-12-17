

class Card:
    id = 0
    winner_numbers = []
    available_numbers = []

    def __init__(self, _id, _winning_numbers, _available_numbers) -> None:
        self.id = _id
        self.winner_numbers = _winning_numbers
        self.available_numbers = _available_numbers