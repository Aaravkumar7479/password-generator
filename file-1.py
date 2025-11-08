

#This tool will generate  a strong passwoed for you according to your needs 
#we will ask you about (length,uppercase,lowercase ,special ,character )
import random
while True :
    print()
    print("  🔥 WELCOME TO  INTERACTIVE PASSWORD GENERATOR TOOL 😎🔥  ")
    print()
    while True :

        try:
            length =int(input("Enter the desired  password length : ")) 
            if length<=0 :
                print("❌ Invalid  input .Length must be a positive number .")
                print()
                continue
            break
        except ValueError :

            print("❌ Invalid  input .Please enter only  numbers .")
            print()
        
    print()


    # .strip() Removes any spaces at the beginning and end of the input.
    # .lowercase() Converts all letters to lowercase. 

    while True :
        case=str(input("Do you want the password in (uppercase /lowercase /mixed) : ")).strip().lower()
        if(case !="lowercase" and case !="uppercase" and case!="mixed") :
            print("❌ Invalid choice .please enter one of the given choices .")
            print()
            continue
        break
    print()
    while True :
        number=str(input("Do you want  number in your password (yes/no) : ")).strip().lower()

        if(number !="yes" and number !="no"):
            print("❌ Invalid choice .please enter one of the given choices .")
            print()
            continue
        break

    print()
    while True :
        s_char=str(input("Do you want special character in your password (yes/no) : ")).strip().lower()

        if(s_char!="yes" and s_char !="no"):
            print("❌ Invalid choice .please enter one of the given choices .")
            print()
            continue
        break
    print()

    chars=[]

    if (case=="lowercase") :

        chars+="abcdefghijklmnopqrstuvwxyz"

    elif (case=="uppercase"):
        chars+="ABCDEFHGHIJKLMNOPQRSTUVWXYZ"
    elif case=="mixed":
        chars+="abcdefghijklmnopqrstuvwxyzABCDEFHGHIJKLMNOPQRSTUVWXYZ"

    if number=="yes" :
        chars+="0123456789"
    elif number=="no":
        chars+=""

    if s_char=="yes":
        chars+="!@#$%^&*(_/<?>)"

    elif chars=="no":

        chars+=""
    lst=[]
    for i in range(1,length+1 ):
        lst.append(random.choice(chars))

    random.shuffle(lst)

    password="".join(lst)
    print(f"Your generated password is 👉  {password}")
    print()

    while True:
        like=str(input("Do you like the given password (yes/no) :")).strip().lower()
        if(like!="yes" and like!="no"):
            print(" ❌ Invalid choice . please enter one of  the given choices . ")
            print()
            continue
        break


    print()    
    if(like=="yes"):
        print("Thank you 😊 .Glad it worked for you .")
    else :
        print("We are sorry 😔 , we didn't meet your expectations .")

    print()

    while True :
        do_again=str(input("Do you want to generate password again (yes/no): ")).lower().strip()
        if(do_again !="yes" and do_again!="no"):
            print("❌ Invalid choice . please enter one of  the given choices .")
            print()
            continue
        break
    if(do_again=="yes"):
        continue 
    else :
        print()
        print("  🎉 Thank you for using our password generator tool 😊 🙌")
        break









    

    

        

    









            



