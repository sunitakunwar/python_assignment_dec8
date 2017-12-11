'''Define a global static password value by yourself.
 Then define a function which prompts user for a password.
 If the password is a match, print "password match" or else print "Wrong password"'''


class Const():
    def password():
        return 1

check=int(input("Enter the password: "))

if (check==1):
    print("password match")
else:
    print("wrong password")