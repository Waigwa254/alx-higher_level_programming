#!/usr/bin/python3

"""Defines a tudent."""


class Student:
    """Represa student."""

    def __init__(self, first_name, last_name, age):
        """Int.
        Args:
            fname of the student.
            llast name of the student.
            audent.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Geary representation of the Student.
              represents only those attributes
         in the list.
        rgs:
        tributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """l s of the Student.
        Ars:
          value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
