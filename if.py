from tempfile import tempdir


tempreture =25

if tempreture >30:
    print("Its a hot day")
    print("Dirnk Plenty of `#water")
elif tempreture >20 :# (20,30])
    print("Its a nice day")
elif tempreture >10 :# (10,20]
    print("It's a bit cold")
else:
    print("It's Cold")
print("done")


weight = int(input("Weight: "))
unit = input("(K)g or (L)bs :").lower()
factor=0.45359237

if unit == 'k' :
    weight_in_pound = weight / factor
    print("Weight in pound : ", weight_in_pound)
elif unit == 'l' :
    weight_in_kg = weight *  factor
    print("Weight in Kg : ", weight_in_kg)
else:
    print("Invalid input")


