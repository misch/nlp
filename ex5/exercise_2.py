#!/usr/bin/python

from exercise_1 import fnv

class Dictionary:
    def __init__(self, initial_capacity):
        self.capacity = initial_capacity
        self.hashes = []

    def insert(self, string):
        self.hashes.append(fnv(string))
        #TODO: throw exception if hash already exists

    def remove(self, string):
        self.hashes.remove(fnv(string))
        #TODO: throw exception if hash doesn't exist

    def lookUp(self, string):
        #TODO
        return string

    def size(self):
        #TODO
        return 0

    def capacity(self):
        return self.capacity