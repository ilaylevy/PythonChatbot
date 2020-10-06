import random as rand
print("prefix is @")
prefix = "@"
userlist = []
commandlist = ["randint", "switchuser", "help"]

def chatbotrun():
    command = input("")
    if command == f"{prefix}help":
        print(f"heres a quick tour\n\n * if you want to change your prefix or even entire commands with this as a\nbase... the code's open source!\n* your prefix is {prefix}, but you can always change it in the code later on\n* all commands are displayed in the {prefix}commands command")
        chatbotrun()
    if command == f"{prefix}randint":
        maxnum = int(input("please enter a max number\n"))
        minnum = int(input("please enter a min number\n"))
        print(rand.randint(minnum, maxnum))
        chatbotrun()
    if command == f"{prefix}switchuser":
        username = input("please enter your username or create a new one\n")
        if username == "new":
            newuser = input("please enter your name\n")
            userlist.append(newuser)
            print(f"welcome {newuser}")
            chatbotrun()
        elif username != userlist:
            print(f"welcome {username}")
            chatbotrun()
    if command == f"{prefix}commands":
        print(commandlist)
        chatbotrun()



chatbotrun()