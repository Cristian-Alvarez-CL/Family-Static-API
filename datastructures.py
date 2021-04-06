
from random import randint
import uuid

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [
            {
                "id" : self._generateId(),
                "first_name" : "John",
                "last_name" : last_name,
                "age" : 33,
                "lucky_numbers": [7, 13, 22]},
            {
                "id" : self._generateId(),
                "first_name" : "Jane ",
                "last_name" : last_name,
                "age" : 35,
                "lucky_numbers": [10, 14, 3]},
            {
                "id" : self._generateId(),
                "first_name" : "Jimmy ",
                "last_name" : last_name,
                "age" : 5,
                "lucky_numbers": [1]}
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return member

    def delete_member(self, id):
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                return self._members
        

    def get_member(self, id):
        for m in self._members:
            if m["id"] == int(id):
                return m

    def get_all_members(self):
        return self._members