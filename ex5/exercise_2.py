#!/usr/bin/python

from exercise_1 import fnv


class Dictionary:
    def __init__(self, initial_capacity):
        self.capacity = initial_capacity
        self.hash_table = [[] for _ in range(initial_capacity)] # generate a list of empty lists with the give capacity

    def insert(self, string):
        position = self.get_key(string)
        hash_values = self.hash_table[position]  # List of strings that are have been mapped to the same hash key.
        if string in hash_values:
            raise Exception('The string {} already exists in the dictionary.'.format(string))

        hash_values.append(string)

        if self.size() > self.capacity/2:
            self.capacity *= 2
            old_hash_table = self.hash_table
            self.hash_table = [[] for _ in range(self.capacity)]
            for hash_values in old_hash_table:
                for s in hash_values:
                    self.insert(s)


    def remove(self, string):
        position = self.get_key(string)
        hash_values = self.hash_table[position]

        if not string in hash_values:
            raise Exception("The string {} is not in the dictionary".format(string))
        hash_values.remove(string)


    def lookUp(self, string):
        position = self.get_key(string)
        hash_values = self.hash_table[position]

        if string in hash_values:
            return string
        return None

    def size(self):
        size = 0
        for x in self.hash_table:
            if x:
                size += 1
        return size

    def capacity(self):
        return self.capacity

    def get_key(self, string):
        return (fnv(string) % self.capacity)