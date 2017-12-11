'''Define a global static password value by yourself.
 Then define a function which prompts user for a password.
 If the password is a match, print "password match" or else print "Wrong password"'''


password="rock"
def checkp(password):
    ans=input("enter the password:")
    if (ans==password):
        print("password match")
    else:
        print("wrong password ")

checkp(password)