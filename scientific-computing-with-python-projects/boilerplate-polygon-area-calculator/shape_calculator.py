
from typing import Any


class Rectangle:

    
    def __init__(self, width: int, height: int):
        self.set_height(height)
        self.set_width(width)

    def set_width(self, width: int) -> None:
        self.width = width
    def set_height(self, height: int) -> None:
        self.height = height
    def get_area(self) -> int:
        return self.width * self.height
    def get_perimeter(self) -> int:
        return 2*(self.width + self.height)
    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2)**.5
    def get_picture(self) -> str:
        if max(self.width, self.height) > 50:
            return "Too big for picture."
        res = ("*"*self.width+"\n")*self.height
        return res
    def get_amount_inside(self, other) -> int:
        x = self.width // other.width
        y = self.height // other.height
        return x*y
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
    
class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)
    
    def __str__(self) -> str:
        return f"Square(side={self.width})"
    def set_side(self, side: int):
        super().set_width(side)
        super().set_height(side)


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))