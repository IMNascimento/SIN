def sm(x):
    if x <= 5:
        return 1
    elif 5 < x <= 10:
        return (10 - x) / 5
    else:
        return 0

def mm(x):
    if 0 <= x <= 5:
        return x / 5
    elif 5 < x <= 10:
        return (10 - x) / 5
    else:
        return 0

def gm(x):
    if x >= 5:
        return 1
    elif 0 <= x < 5:
        return x / 5
    else:
        return 0