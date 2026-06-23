# ex 1 
values = [450, 850, 1200, 650, 1600]

print(len(values))

print(sum(values))

moyenne = sum(values) / len(values)
print(moyenne)

print(min(values))

print(max(values))



# ex 2 
consomation = [450, 850, 1200, 650, 1600]
let = []
for i in consomation:
    if i > 1000:
        let.append(i)

print(let)


# ex 3 
etudiant = {
    "name" : "ayoub",
    "age" : 21,
    "ville" : "safi",
    "nbr_heures_etudes": 2,
    "is_active" : True
}

for key , value in etudiant.items():
    print(f"{key} : {value}")

# ex 4 
unite = [
    {
        "nom" : "pp1",
        "ville" : "safi",
        "consommation" :321 ,
        "status": "active"
    },
    {
        "nom" : "pp2",
        "ville" : "jdida",
        "consommation" : 231 ,
        "status" : "incative"
    },
    {
        "nom" : "np1" ,
        "ville" : "tetouna",
        "consommation" : 8439,
        "status" :"active"
    }, 
]


for i in unite :
    if i["status"] == "active" :
        print(i["nom"])

for i in unite :
    if i["consommation"] > 1000:
        print(i["nom"])

consomation_total = 0;
for i in unite :
    consomation_total =+ i["consommation"];

print(consomation_total);
