# function output k in natural degree

def power(k, n):
    try:
        n = int(n)
        if n < 0:
            return -1
        if k != 0:
            if n == 0:
                return 1
            elif n < 0:
                return 1 / power(k, -n)
            else:
                return k * power(k, n - 1)
        else:
            return 0
    except BaseException:
        return -1


def sqrt(n, l=1, r=0):
    try:
        if n < 0:
            return -1
        elif 1 > n > 0:
            return 1 / sqrt(1 / n)
        else:
            if r == 0:
                r = n
            while r - l > 0.00000000000001:
                if (r + l) / 2 * (r + l) / 2 < n:
                    return sqrt(n, (r + l) / 2, r)
                elif (r + l) / 2 * (r + l) / 2 > n:
                    return sqrt(n, l, (r + l) / 2)
                else:
                    return (r + l) / 2
            return r
    except BaseException:
        return -1

