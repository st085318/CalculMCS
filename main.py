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

    def power(self, n):
        try:
            value = self.value
            n = int(n)
            if self.value != 0:
                if n == 0:
                    self.value = 1
                elif n < 0:
                    calc = Calculator(self.value)
                    self.value = 1 / calc.power(-n).value
                else:
                    for i in range(n-1):
                        self.value = self.value * value
                return self
        except BaseException:
            self.value = value
            return self

    def sqrt(self):
        try:
            if self.value < 0:
                return self
            elif 1 > self.value > 0:
                l = 0
                r = 1
            else:
                r = self.value
                l = 0
            while r - l > 0.000000000001:
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




if __name__ == '__main__':
    calculator = Calculator(2)
    #print(calculator)
    #print(calculator.add(1, 2, 3, 5.1).multiply(4, 0.123).subtract(4, 1, -100).divide(5, integer_divide=True))
    print(calculator.power(-2).value)
    #print(Calculator(100) + 10)
    #print(10 + Calculator(12))
    #print(Calculator(123) - Calculator(14))
    #print(Calculator(14) / Calculator(2))

