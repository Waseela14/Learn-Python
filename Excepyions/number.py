try:
    x= int(input("What is x:"))
    print(f"X is {x}")    # instead of writting it here we can wite it inside else shown below  
except ValueError:
    print("x is not integer") 
else:
    print(f"X is {x}")       