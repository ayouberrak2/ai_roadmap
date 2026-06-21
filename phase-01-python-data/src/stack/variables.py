# =================
# VARIABLES 
# ==============

student_name = "Ayoub"
age = 24

print(f"non : {student_name}")
print(f"age : {age}")


# ============================
# TYPES DE DONNÉ
# =======================

city = "Marrakech"              # str
number_of_units = 5             # int 
electricity_price = 1.25        # float 
is_active = True                # bool
operator_name = None            # absence de valeur

print("\n--- Types des variables ---")
print(f"Type de city : {type(city)}")
print(f"Type de number_of_units : {type(number_of_units)}")
print(f"Type de electricity_price : {type(electricity_price)}")
print(f"Type de is_active : {type(is_active)}")
print(f"Type de operator_name : {type(operator_name)}")


# ===================
# OPERATIONS 
# ========================

consumption_kwh = 1250.5
price_per_kwh = 1.25

total_cost = consumption_kwh * price_per_kwh

print("\n--- Calcul de consommation ---")
print(f"Consommation : {consumption_kwh:.2f} kWh")
print(f"Prix par kWh : {price_per_kwh:.2f} DH")
print(f"Coût total : {total_cost:.2f} DH")


# =================
# CONVERSION DES TYPES
# =======================

age_as_text = "24"
age_as_number = int(age_as_text)

price_as_text = "1.25"
price_as_number = float(price_as_text)

number_as_text = str(100)

print("\n--- Conversion des types ---")
print(f"Âge converti : {age_as_number}")
print(f"Type de l'âge converti : {type(age_as_number)}")

print(f"Prix converti : {price_as_number}")
print(f"Type du prix converti : {type(price_as_number)}")

print(f"Nombre converti en texte : {number_as_text}")
print(f"Type du nombre converti : {type(number_as_text)}")


# ====================
# INPUT
# ======================

unit_name = input("\nEntre le nom de l'unité : ")
consumption = float(input("Entre la consommation en kWh : "))
price = float(input("Entre le prix par kWh : "))

cost = consumption * price

print("\n--- Résultat saisi par l'utilisateur ---")
print(f"Unité : {unit_name}")
print(f"Consommation : {consumption:.2f} kWh")
print(f"Coût total : {cost:.2f} DH")
