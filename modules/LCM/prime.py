#!/usr/bin/python3
import math
class Prime:
    """A class which can calculate next prime numbers"""
    def __init__(self):
        self.num = 2

    def get(self):
        return self.num

    def is_prime(self,num):
        upper_limit = int(math.sqrt(num)) + 1
        for i in range(2,upper_limit,2):
            if num % i == 0:
                return False
        return True

    def next(self):
        self.num = self.num + 1
        while(not self.is_prime(self.num)):
            self.num = self.num + 1
        return self.num
