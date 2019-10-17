user = "admin"
user_count = 0
pw = "admin"
pw_count = 0

while True:
	name = input("Enter your name: ")
	if name != user:
		print("Invalid user")
	if name != user:
		user_count = user_count + 1
	if user_count == 3:
		print("Maximum number exceeded")
		quit()
	if name == "admin":
		continue
	password = input("Enter your password: ")
	if password != pw:
		print("Invalid credentials")
	if password != pw:
		pw_count = pw_count + 1
	if pw_count == 3:
		print("Maximum number exceeded")
		quit()
	if password == pw:
		break

print("Welcome %s" % user)