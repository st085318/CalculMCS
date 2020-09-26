# function output k in natural degree

class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value

    def add(self, *args):
        try:
            self.value += sum(args)
            return self
        except BaseException:
            return -1

    def multiply(self, *args):
        try:
            for x in args:
                self.value *= x
            return self
        except BaseException:
            return -1

    def divide(self, *args, integer_divide=False):
        try:
            for x in args:
                if integer_divide:
                    self.value //= x
                else:
                    self.value /= x
            return self
        except ZeroDivisionError:
            return -1
        except BaseException:
            return -1

    def power(self, degree):
        try:
            value = self.value
            degree = int(degree)
            if self.value != 0:
                if degree == 0:
                    self.value = 1
                elif degree < 0:
                    calc = Calculator(self.value)
                    self.value = 1 / calc.power().value
                else:  # degree is natural, so we multiply self degree times
                    for i in range(degree-1):
                        self.value = self.value * value
                return self
            return self
        except BaseException:
            self.value = value
            return self

    def root(self):
        try:
            if self.value < 0:
                return self  # can not root from negative number
            elif 1 > self.value > 0:  # l = left, r = right border
                l = 0
                r = 1
            else:
                r = self.value
                l = 0
            while r - l > 0.000000000001:  # binary search
                if (r + l) / 2 * (r + l) / 2 < self.value:
                    l = (r+l)/2
                elif (r + l) / 2 * (r + l) / 2 > self.value:
                    r = (r+l)/2
                else:
                    self.value = (r+l)/2
                    return self
            self.value = (r+l)/2
            return self
        except BaseException:
            return -1

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)


