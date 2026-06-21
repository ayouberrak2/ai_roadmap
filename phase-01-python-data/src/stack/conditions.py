# ======================
# CONDITIONS
# ===========================

consumption = 1250

if consumption > 1000:
    print("La consommation est élevée.")


# ==============
# IF ELSE
# =================

temperature = 18

if temperature >= 20:
    print("La température est agréable.")
else:
    print("La température est basse.")


# ==========================
# IF ELIF ELSE
# ===================

consumption = 1250

if consumption > 1500:
    consumption_level = "critique"
elif consumption > 1000:
    consumption_level = "élevée"
elif consumption > 500:
    consumption_level = "moyenne"
else:
    consumption_level = "faible"

print(f"Niveau de consommation : {consumption_level}")


# ===================
# COMPARAISON
# =====================

value = 1000

print("\n--- Comparaisons ---")
print(value == 1000)   # égal à
print(value != 500)    # différent de
print(value > 500)     # supérieur à
print(value < 1500)    # inférieur à
print(value >= 1000)   # supérieur ou égal à
print(value <= 1000)   # inférieur ou égal à


# ==========
# AND
# =======================

consumption = 1200
is_active = True

if consumption > 1000 and is_active:
    print("\nAlerte : unité active avec consommation élevée.")


# ==============
# OR
# ===========

status = "maintenance"

if status == "inactive" or status == "maintenance":
    print("L'unité n'est pas disponible.")


# ==============
# NOT
# ========

is_active = False

if not is_active:
    print("L'unité est inactive.")

