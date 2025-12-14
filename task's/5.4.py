class Pencil:
    def __init__(self, color: str, length: int):
        self.color = color
        self.length = length

    def sharpen(self):
        self.length -= 1

    def __str__(self):
        return f'Color: {self.color}, Length: {self.length}'

pencil = Pencil('yellow', 10)
print(pencil)
pencil.sharpen()
print(pencil)