#!/usr/bin/python3
from abc import ABC, abstractmethod

#An abstract base class for different type of parameter extraction modules
class ExtractParameters(ABC):

    @abstractmethod
    def extract_and_solve(self,question):
        pass
