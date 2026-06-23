# ============================
# dictionaire ==> cle : value
# ============================

me = {
    "name":"ayoub",
    "age":21,
    "taille":181,
    "niveau":"bac+3"
}


# =======
# get()
# ======
# Si la clé n’existe pas, get() retourne None au lieu de provoquer une erreur.

name = me.get("name");
print(name)


# =================
# modify and add
# =================

me["name"] = "ERRAK" # modify

me["is_student"] = True # add 

del me["niveau"] # delete


# ======================
# for in dict
# ======================


for key in me :
    print(key)

for value in me.values():
    print(value);

for keys , values in me.items():
    print(f"{keys} : {values}")




# ============== 
# list de dict
# ==============



all = [
    {
        "name":"name1",
        "age":21,
        "nationalite":"marocaine"
    },
    {
        "name":"name2",
        "age":22,
        "nationalite":"francais"
    },
    {
        "name":"name3",
        "age":23,
        "nationalite":"algeriane"
    }
]

for i in all :
    print(f"{i["name"]} a {i["age"]} , il est {i["nationalite"]}")
