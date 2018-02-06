def area(base, height):

    if base < 0 or height < 0:
        raise ValueError('value error')

    area = base * height /2

    return area