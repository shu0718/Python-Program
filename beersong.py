word="bottles"
for beer_num in range(-10,-20,-1):
    print(beer_num,word,"of beer on the wall")
    print(beer_num,word,"of beer")
    print("take it down")
    print("Pass it around")
    if beer_num==1:
        print("no more bottles of beer on the wall")
    else:
        new_num = beer_num-1
        if new_num == 1:
            word = "bottle"
        print(new_num,word,"of bear on the wall")
    print()
              
