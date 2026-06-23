# ==============
#  les listes
# ===================

number = [1,23,4,5,6,7];
number.append(21);
number.insert(0,121);
number.remove(1)
last = number.pop();
print(last)
print(len(number));
print(sum(number));
print(min(number));
print(max(number));
number.sort(reverse=True)
print(number);


# ===========
#  split
# ===========


num = [1,2,3,4,5,6,7,8,9];
print(num[2:3])
print(num[2:]) # depuis 2
print(num[:-1]) # sauf le dernier
print(num[::-1]); # afficher l'inverse

# =========
# for
# ==========

exemple = [1,3241,4124,143,12,42134,2];
for i in exemple :
    fois3 = i*3;
    print(fois3)

consumptions = [450, 700, 1200, 850, 1600]




for consumption in consumptions:
    if consumption > 1500:
        print(f"{consumption} kWh : critique")
    elif consumption > 1000:
        print(f"{consumption} kWh : élevée")
    elif consumption > 500:
        print(f"{consumption} kWh : moyenne")
    else:
        print(f"{consumption} kWh : faible")



for j in range(10):
    print(j);

for n in range(1, 6): # de 1 a 6
    print(n)

for u in range(1,10,2): # de 1 a 10 avec un pas de 2
    print(u);



# ==============
# enumerate
# ============

citys = ["safi","casa","rabat"];

for index , city in enumerate(citys):
    print(index,city)

for index , cit in enumerate(citys, start=1): #pour commancer les index de 1
    print(index,cit)


# ===========
# zip
# ===============

users = ["ayoub","salah","mohamed"];
ages = [12,23,42];

for user,age in zip(users , ages):
    print(f"{user} a {age} ans")


# =============
# break et continue
# ====================

consumptions = [450, 700 , -12, 1600, 850]

for consumption in consumptions:
    if consumption > 1500:
        print("trouve")
        break

    print(consumption)


for consumption in consumptions:
    if consumption < 0:
        continue # il sote la valeur dont il ne fait pas la condition

    print(consumption)



# =========
# while
# =========

counter = 1

while counter <= 5:
    print(counter)
    counter += 1

consumption = -1


while consumption < 0:
    consumption = float(
        input("Entre une consommation positive : ")
    )

print(f"Valeur acceptée : {consumption}")
