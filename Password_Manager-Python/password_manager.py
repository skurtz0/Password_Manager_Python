def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data =line.rstrip()
            user, pwd = data.split("|")
            print ("Email/Username: ", user, "Password: " , pwd )

def add():
    name = input("Username/E-mail: ") 
    pwd = input("Pasword: ") 

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    choose = input("Add a new password or view the passwords / add , view or quit:   ")
    if choose == "quit":
        break

    elif choose == "view":
        view()

    elif choose == "add":
        add()

    else: 
        print("Error")
        continue
