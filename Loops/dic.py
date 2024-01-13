#mem = {"W":"Waseela", "M":"Muneer","S":"Sohana","A":"Anila","Al":"Ali Hassan"}

# it can also write as,
''' mem = {
    "W":"Waseela", 
    "M":"Muneer",
    "S":"Sohana",
    "A":"Anila",
    "Al":"Ali Hassan"
    }  '''
# for i in mem: # here i indicates key and mem[i] indicate key value
#      print(i, mem[i], sep=", ") 
#      print(mem["W"] )
    
    
    # we can add more info in dic 
    
stu =[
    {"name":"waseela", "class":"3rd year", "email":"waseela@g.com", "ph":"0376583"},
    {"name":"muneer", "class":"1st year", "email":"muner@" ,"ph":"0319548"},
    {"name":"sohana", "class":"1st year", "email":"sohna@g.com", "ph":"05447"},
    {"name":"anila", "class":"9th", "email":"anila@g.com" ,"ph":"08767564"},
    {"name":"Ali hassan", "class":"8th", "email":"ali@g.com" ,"ph":"035462527"}
]
for i in stu:
    print(stu["name"], stu["class"], stu["email"],stu["ph"])
     