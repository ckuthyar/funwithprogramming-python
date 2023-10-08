def find_angle(x,y):
    if x > 12:
        x = x - 12
    hr_hand = (x * 30) + (y * 0.5)
    min_hand = y * 6

  
    diff = hr_hand - min_hand
    if diff < 0:
        diff = -(diff)
    if diff == 360:
        diff = 0
    print(diff)
    return diff

timee = input("Enter Time : " )
x,y = timee.split(":")

print(find_angle(int(x), int(y)))
