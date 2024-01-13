def main():
    x = int(input("what is the number: "))
    if is_even(x):
        print("No is Even")
    else:
        print("No is Odd")
        
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
main()                