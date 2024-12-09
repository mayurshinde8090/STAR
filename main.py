import admission as AD
import tc as TC

while True:
    print("|________________Welcome to STAR_________________|")
    print("\t\t1. Admission Register")
    print("\t\t2. TC Register")
    print("\t\t3. Exit")
    print("|________________________________________________|")

    choice = int(input("Enter your choice(1-3):"))
    if choice==1:
        AD.MenuAdmn()
    elif choice==2:
        TC.Menu_TC()
    elif choice==3:
        print("Thanks for using STAR.")
        input("Press any key to exit.")
        break
    else:
        input("Incorrect choice. Press any key to continue and RE-enter.") 
