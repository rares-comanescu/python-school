name = input("Enter your name\n>") # Get the name
print ("Hello %s, my name is Mr. Robot" % name) 
age = int(input("Tell me your age %s\n>" % name)) # Get the date
to_go = 100 - age
print("So you know %d more years until 100" % to_go)
print("That will be around year %d" % (2019+to_go))
