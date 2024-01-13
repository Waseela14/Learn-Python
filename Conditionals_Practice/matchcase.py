name = input("enter your name: ")
match name:
    case "Khadim Hussain" | "Fatima":         # "|" used for "or"
        print("Parent")
    case "waseela":
        print("Elder Sister")
    case "Muneer Abbas":
        print("Elder Brother")
    case "Sohana":
        print("Middle Sister")
    case "Anila":
        print("younger sister")  
    case "Ali Hassan":
        print("Younger Brother")
    case _:                          # case _:  use foe anything else
        print("Not Family Member")                  
    