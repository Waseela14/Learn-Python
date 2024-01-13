print("Amount due: 50")
a = 0
while True:

    if a !=50:
        price =int(input("Insert Coin: "))
        
        if price == 25 or price == 10 or price == 5:
            a+=price      
            new_price = 50-a
            print("Anount Due:",new_price)
        else:
            print("Insert a Coint of 25 or 10 or 5") 
            
    else:
        break        