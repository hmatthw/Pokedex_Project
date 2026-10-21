""" def slot(q, x, y, z):
    count = 0
    current = q
    while current > 0:
        if current > 0:
            current -= 1
            x +=1
            count += 1
        if x == 35:
            current += 30
            x = 0
        if current > 0:
            current -=1
            y += 1
            count += 1
        if y == 100:
            current += 60
            y = 0
        if current > 0:
            current -=1 
            count +=1
            z += 1
        if z == 10:
            current += 9
            z = 0
        if current == 0:
            print(count)
slot(77, 4, 9, 3) """

def slot(q, x, y, z):
    count = 0
    current = q
    while current > 0:
        current -= 3
        count += 3
        x += 1
        y += 1
        z += 1
    if x == 35:
        current += 30
        x = 0
    if y == 100:
        current += 60
        y = 0
    if z == 10:
        current += 9
        z = 0
    print(count)
slot(77, 4, 9, 3)