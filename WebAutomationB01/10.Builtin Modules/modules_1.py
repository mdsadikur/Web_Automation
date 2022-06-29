import math
from math import fsum


class ModulesDemo():
    def builtin_modules_fsum(self):
        num = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
        print(fsum(num))  # imported from math

    def builtin_modules_sqrt(self):
       print(math.sqrt(25))   # imported from math


obj = ModulesDemo()
obj.builtin_modules_fsum()
obj.builtin_modules_sqrt()