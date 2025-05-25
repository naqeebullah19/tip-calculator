print("Welcome to the tip calculator")
bill=float(input("how much was your bill? :"))
tip=int(input("How much percent tip you want to give, 10%, 12%, 15% ?"))
person=int(input("How much person are splitting the bill? "))

if tip==10:
    print(f"each persons share is :{(bill+bill/10)/person}")
elif tip==12:
    print(f"each persons share is :{(bill+bill/12)/person}")
elif tip==15:
    print(f"each persons share is :{(bill+bill/15)/person}")
else:
    print("please select values according to the given limit")
