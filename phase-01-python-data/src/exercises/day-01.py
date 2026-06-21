unit_name = "Unité Marrakech"
consumption_kwh = 1250.5
price_per_kwh = 1.25


total_consomation = consumption_kwh*price_per_kwh

# print(unit_name+" a consomee "+str(total_consomation));
# print(f"{unit_name} a consomee {total_consomation}")

# age = int(input("taper votre age : "));
# print(f"ton age est : {age}")

# ex 1
non = input("taper  votre non : ");
date_naissance = int(input("taper  votre non : "));

age = 2026-date_naissance;

print(f"je suis {non} j'ai {age} ans")


# ex 2
celsius = input("taper la tempairature en celisuis :");

far = celsius*9/5+32;
print(far);


# ex 3 

nbr = int(input("taper le nombre :"))

if(nbr%2 == 0):
    print("le nombre est pair")
else:
    print("le nombre est inpair")


# ex 4 
consommation = int(input("taper la consommation : "));

if(consommation>0 and consommation<500):
    print("faible ")
elif(consommation>501 and consommation<1000):
    print("moyyene ")
elif(consommation>1001 and consommation<1500):
    print("elevee")
elif(consommation>1500):
    print("critique")