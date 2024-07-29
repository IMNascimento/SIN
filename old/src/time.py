def mc(y):
    if y <= 15:
        return 1
    elif 15 < y <= 30:
        return (30 - y) / 15
    else:
        return 0

def c(y):
    if 0 <= y <= 15:
        return y / 15
    elif 15 < y <= 30:
        return (30 - y) / 15
    else:
        return 0

def m(y):
    if 15 <= y <= 30:
        return (y - 15) / 15
    elif 30 < y <= 45:
        return (45 - y) / 15
    else:
        return 0

def l(y):
    if 30 <= y <= 45:
        return (y - 30) / 15
    elif 45 < y <= 60:
        return (60 - y) / 15
    else:
        return 0

def ml(y):
    if y >= 45:
        return 1
    elif 30 <= y < 45:
        return (y - 30) / 15
    else:
        return 0