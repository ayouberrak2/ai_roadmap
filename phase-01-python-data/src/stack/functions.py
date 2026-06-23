# ===================
#  function
# ===============


# éviter la répétition ;
# donner un nom à une logique ;
# simplifier le programme ;
# tester une partie indépendamment ;
# réutiliser le code ;
# corriger une logique à un seul endroit


def print_f(non : str , age : int)->None:
    print(f"{non} a {age}")

print_f("ayoub",21);

print_f(
    non="ayoub",
    age=21
    );

# ==========
# Type hints
# ==========


def calculate_cost(
        name : str,
        consomation : float ,
        durre : int,
        values: list[float],
        operator_name: str | None

)->float: # int bool str
    return consomation*durre



# =======================
#  Variables locales
# =====================


def calculate_cost(consumption: float, price: float) -> float:
    total_cost = consumption * price

    return total_cost

# total_cost existe seulement dans la fonction.

# ===============================================================
# Éviter les variables globales !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ===============================================================

