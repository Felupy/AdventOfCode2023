

class Card:
    id = 0
    winner_numbers = []
    available_numbers = []

    def __init__(self, _id, _winning_numbers, _available_numbers) -> None:
        self.id = _id
        self.winner_numbers = _winning_numbers
        self.available_numbers = _available_numbers

    def get_matching_numbers(self):
        matching_numbers = []
        for number in self.winner_numbers:
            if number in self.available_numbers:
                matching_numbers.append(number)
        
        return matching_numbers