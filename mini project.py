t = 0
n = 1


def bill():
    global t
    print("Your Bill is: ", t, '\n')


def cash():
    c = 0
    c = int(input("Enter Cash:"))
    if(c >= t):
        print("Received Cash: ", c, '\n')
        rc = c-t
        print("Returned Cash = ", rc, '\n')
        print(int(rc/2000), " notes of 2000 \n")
        print(int(rc % 2000/500), " notes of 500 \n")
        print(int(rc % 2000 % 500/200), " notes of 200 \n")
        print(int(rc % 2000 % 500 % 200/100), " notes of 100 \n")
        print(int(rc % 2000 % 500 % 200 % 100/50), " notes of  50 \n")
        print(int(rc % 2000 % 500 % 200 % 100 % 50/20), " notes of  20 \n")
        print(int(rc % 2000 % 500 % 200 % 100 % 50 % 20/10), "notes of  10 \n")
        print(int(rc % 2000 % 500 % 200 % 100 % 50 % 20 % 10/5), " notes of   5 \n")
        print(int(rc % 2000 % 500 % 200 % 100 % 50 % 20 % 10 % 5/2), " notes of   2 \n")
        print(int(rc % 2000 % 500 % 200 % 100 % 50 % 20 % 10 % 5 % 2/1), " notes of   1 \n")
    else:
            print("!!!Please Enter valid amount!!!\n")
            cash()


def menu():
    global n, t 
    print("\t\t:::::::::::::::WELCOME TO MY HOTEL MOONLIGHT:::::::::::::::\n")
    while(n):
        print("::::::::::MENU::::::::::\n")
        print("1. Samosa                  25/-\n")
        print("2. Dosa                    45/-\n")
        print("3. Chai                    20/-\n")
        print("4. Coffee                  30/-\n")
        print("5. Chicken kabab          130/-\n")
        print("6. Paneer Tikka           130/-\n")
        print("7. Momos                   90/-\n")
        print("8. Manchurian             110/-\n")
        print("0. Exit                        \n")
        n = int(input("Please Enter Your Choice: "))
        if(n == 1):
            print("Ok Nice Choice.....\n")
            p = int(input("How Many Plates- "))
            t = t+(p*25)
        elif(n == 2):
            print("Ok Nice Choice.....\n")
            p = int(input("How Many Plates- "))
            t = t+(p*45)
        elif(n == 3):
            print("Ok Nice Choice.....\n")
            p = int(input("How Many Plates- "))
            t = t+(p*20)
        elif(n == 4):
            print("Ok Nice Choice.....\n")
            p = int(input("How Many Plates- "))
            t = t+(p*30)
        elif(n == 5):
            print("Ok Nice Choice.....\n")
            p = int(input("How Many Plates- "))
            t = t+(p*130)
        elif(n == 6):
            print("Ok Nice Choice.....\n")
            p = int(input("How Many Plates- "))
            t = t+(p*130)
        elif(n == 7):
            print("Ok Nice Choice.....\n")
            p = int(input("How Many Plates- "))
            t = t+(p*90)
        elif(n == 8):
            print("Ok Nice Choice.....\n")
            p = int(input("How Many Plates- "))
            t = t+(p*110)
        elif(n == 0):
            bill()
            cash()
            n = 0
        else:
            print(
                "Kripaya Menu me diye gaye items hi chune Fukat ki hosiyari na kare  \n")



menu()
