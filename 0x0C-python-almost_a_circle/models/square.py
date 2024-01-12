#!/usr/bin/python3
"""the square is defined."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rep a sqre."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiew Square.

        Args:
            sizeof the new Square.
            x (i of the new Square.
            y (ithe new Square.
            id of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/ Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating  Square.

        Args:
            *arute values.
               tribute
               size attribute
               e
                y attribute
            **kairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return tpresentation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
