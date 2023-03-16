def average(a):
    if(len(a) == 0):
        raise NameError('IligalArgumentException')
    sum = 0
    for i in a:
        sum += i


    return sum/len(a)