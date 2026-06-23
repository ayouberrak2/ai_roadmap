# ====================
# set
# ================


# Un ensemble stocke des valeurs uniques.

# supprimer les doublons ;
# vérifier rapidement si une valeur existe ;
# comparer des groupes de valeurs.


cities = {"Safi", "Marrakech", "Agadir"}

# Les doublons sont automatiquement supprimés

city = {
    "Safi",
    "Marrakech",
    "Safi",
    "Agadir",
}

# print(city)


# =======================
# Ajouter et supprimer
# ===================

cities.add("Casablanca")
cities.remove("Safi")


# ===============
# autre
# =================

# verifi valuer
# if "Marrakech" in cities:
#     print("La ville existe")



active_cities = {"Safi", "Marrakech", "Agadir"}
alert_cities = {"Marrakech", "Casablanca"}

# affiche le commun entre les 2 set
print(active_cities & alert_cities)

# afficher les non communs entre 2 set
print(active_cities | alert_cities)

# afficher les element ajouter dans active_cities
print(active_cities - alert_cities)
