import re


class WordCounter:
 #Method to count total number of uppercase letters in the given string
    def count_uppercase(self, text):
        return sum(1 for char in text if char.isupper())