price1=float()
price2=float()
ex1=int()
ex2=int()
d=float()
largest=float(-99999.99)
for i in range(0,3):
    price1=float(input("kindly enter price of item in supermarket 1"))
    price2=float(input("kindly enter price of item in supermarket 2"))
    if price1>price2:
        d=price1-price2
        d_round=round(d,2)
        print("the difference between 2 items is:", d_round) 
        ex1=ex1+1
        if d>largest:
            largest=d
    elif price2>price1:
        d=price2-price1
        d_round=round(d,2)
        print("the difference between 2 items is:", d_round) 
        ex2=ex2+1
        if d>largest:
            largest=d
print(ex1, "items were more expensive in super market 1")
print(ex2, "items were more expensive in super market 2")
print("largest difference in all above items was:", largest)
        
    
