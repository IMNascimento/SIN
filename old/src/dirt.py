def ps(x):
    if x <= 5:
        return 1
    elif 5 < x <= 10:
        return (10 - x) / 5
    else:
        return 0

def ms(x):
    if 0 <= x <= 5:
        return x / 5
    elif 5 < x <= 10:
        return (10 - x) / 5
    else:
        return 0

def gs(x):
    if x >= 5:
        return 1
    elif 0 <= x < 5:
        return x / 5
    else:
        return 0