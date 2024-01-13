# while True:
#     try:
#         no= int(input("Enter the number:"))
#     except ValueError:
#         print("number is not integer")
#     else:
#         break
# print(f"the number is {no}")   
  
# except:
# except  ZeroDivisionError:
# except SyntaxError:
# except TypeError:     raised when function or oporation is applied to incorrect type
# except ValueError:    when function get argument of correct type but improper ValueError
# except IndexError:    when index of sequence is out of range
# except KeyError:      when key is not found in dic       
            
def deep(inp):
    while True:
        inp=input("What is the answer to the great question of Life, the Universe and Everything?: ")
        # inp = "forty-two"
        # inp= "forty two"
        if inp  == 42 or inp == "forty-two" or input == "forty two":
            break
        else:
            print("No")
            
    print("Yes!")         