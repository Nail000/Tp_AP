people = int(input("How many people need a ride ? "))
taxiSize = int(input("How many people fit in one taxi ? "))

if (people % taxiSize == 0) :
    print("number of taxis nedded :",people // taxiSize)
else :
    print("number of taxis nedded :",(people // taxiSize)+1)