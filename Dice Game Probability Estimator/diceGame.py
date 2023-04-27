import random

def game():
    #dice 1, 2
    D1 = random.randint(1,6)
    D2 = random.randint(1,6)

    fail = [2,3,12]

    win = [7,11]

    if (D1+D2) in fail:
        x = 1
        return x
    if (D1+D2) in win:
        x = 0
        return x
    else:
        initial = D1+D2
        point = 1


    #roll for point


        
    while point == 1:
        D1 = random.randint(1,6)
        D2 = random.randint(1,6)
      
        
        if (D1+D2) == initial:
            x = 1
            return x

        if (D1 + D2) == 7:
            x = 0
            return x
