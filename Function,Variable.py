name=input("What is your name?:")
print("Hello,",name)
 #  "end"  used to add something in the end of any string
print("Hello,",name,end="???")
# 'sep' is used to seprate 
print("Hello,",name, sep="???")

# 'split()' used to seprate words e.g firsrt and last name 
first, last = name.split()
print(first) #it will print only first name

 # .strip() used to remove white spaces from string
name = name.strip()  #remove spaces from name

# .capitalize() used to capitalize first latter of firt word in name string
name = name.capitalize()

# .title() used to capitalize the first latter of every word in ny name or in any title
name = name.title()

print("hello,{name}")
# OUTPUT= hello,{name}
print(f'hello,{name}') # f indicates that { } is nothing but our own formate to write it

# we can use multiple functions simultaneously or in single line
name = name.strip().title()

