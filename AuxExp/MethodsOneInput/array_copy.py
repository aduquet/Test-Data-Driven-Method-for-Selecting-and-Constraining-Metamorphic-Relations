def array_copy(data):

    if(type(data) != "<class 'list'>"):
        raise NameError('data sequence must contain at least two values.')
    b = []
    for i in data:
        b.append(i)

    return b
