def bank():
    inp=input("Greeting: ")
    if inp == "Hello..." or inp == "hello...":
        print("$0")
    elif inp == "H..." or inp == "h..." and inp != "Hello..." and inp != "hello..." :
        print("$20")
    else:
        print("$100") 
bank()            
