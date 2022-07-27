
print("Welcome to SPGA-CGPA Calculator")
type1=int(input("Enter 1.For Percentage 2.For Ponits:"))
if type1==1:
    cgpa=float(input("Enter CGPA:"))
    if cgpa > 0 and cgpa <= 10.75:
        percentage=cgpa-0.75
        temp=percentage*10
        print('----------------------------------')
        print ("You have percentage:",temp,'%')
        print('----------------------------------')
        print("Thank You.......")
    else:
        print('Invalid cgpa')
elif type1==2:
    spga=float(input('Enter your SPGA:'))
    if spga > 0 and spga <= 100:
        temp1=spga/10
        points=temp1 + 0.75
        print('----------------------------------')
        print ("You have CGPA:",points,'points')
        print('----------------------------------')
        
        print("Thank You.......")
    else:
        print('Invalid sgpa Enterd')
else:
    print('Invalid Option Enterd')
    print("Thank You")
print('Made By ❤ Rajesh korlapati')
