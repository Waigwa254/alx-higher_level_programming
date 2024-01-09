!/usr/bin/python3
"""DStudent."""


class Student:
    """Represudent."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            fr): The first name of the student.
            lt_name (str): The last name of the student.
            a the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gerepresentation of the Student.
        If atist of strings, represents only those attributes
        included in the list.
        Args:            attonal) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
