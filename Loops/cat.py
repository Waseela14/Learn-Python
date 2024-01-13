# while True:
#     n = int(input("enter the number: "))
#     if n > 0 :
#         break
# for i in range(n):
#     print("meow")    
    
    # we can write same code using functions
    
def main():
    number = get_no()
    meow(number)

def get_no():
    n = int(input("What's a no: "))
    while True:
        if n > 0 :
            break      # tu use bresk is our own choice
    return n    
           
def meow(n):
    for i in range(n):
        print("meow")
     
    
main()           