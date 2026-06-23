# =================
# exeption
# =================



try :
    age = int("bonjour")
except ValueError :
    print("l'age est un nombre")


try:
    moy = 9/0
except ZeroDivisionError :
    print("la division sur 0 est impossible ")


# ===========================================================
# Lever une exception avec raise
# =======================================


def test(age: int) -> None:
    if age < 0:
        raise ValueError("l'age ne peut pas etre negative")

try:
    test(-1283)
except ValueError as e:
    print(e)



# ===========================
# exemple 
# ==================


try :
    agee = int(input("taper votre age "));
except ValueError :
    print("age doit etre un nombre ")
else :
    print(f"votre age est {agee}")
finally :
    print("fin de traitemant ")

# try : code pouvant échouer ;
# except : traitement de l’erreur ;
# else : exécuté si aucune erreur ;
# finally : exécuté dans tous les cas.

