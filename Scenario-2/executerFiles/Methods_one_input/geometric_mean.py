import math


def geometric_mean(a):
    product = 1
    try:
        for i in a:
            product *= i

        return math.pow(product, 1/len(a))
    except:

        return 'd/0'