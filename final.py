# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Welcome to SPGA-CGPA Calculator")
type1=int(input("enter 1.for cgpa 2.for sgpa:"))
if type1==1:
    cgpa=float(input("enter cgpa:"))
    if cgpa > 0 and cgpa <= 10:
        percentage=cgpa-0.75
        temp=percentage*10
        print('----------------------------------')
        print ("you have percentage:",temp,'%')
        print('----------------------------------')
        print("Thank You.......")
    else:
        print('Invalid cgpa')
elif type1==2:
    spga=float(input('Enter your sgpa:'))
    if spga > 0 and spga <= 100:
        temp1=spga/10
        points=temp1 + 0.75
        print('----------------------------------')
        print ("you have CGPA:",points,'points')
        print('----------------------------------')
        
        print("Thank You.......")
    else:
        print('Invalid sgpa Enterd')
else:
    print('Invalid Option Enterd')
    print("Thank You")
print('Made By Rajesh korlapati')