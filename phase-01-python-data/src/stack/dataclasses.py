# ==================
#  dataclasses
# ===============

# Une dataclass est une classe conçue principalement pour stocker des données.

from dataclasses import dataclass,field

@dataclass
class Consumption:
    unit_name:str
    electricity:float
    water :float

    def calculate_cost(self) -> float:
        return self.electricity * self.water

# La dataclass a automatiquement généré le constructeur.

consumption = Consumption(
    unit_name="Unité Safi",
    electricity=850,
    water=300,
)
# Permet d’afficher clairement l’objet :
print(consumption)


@dataclass
class Student:
    name: str
    age: int
    courses: list[str] = field(default_factory=list) #Chaque étudiant possède sa propre liste.

# default_factory crée une nouvelle valeur pour chaque objet.

# Permet de comparer deux objets selon leurs valeurs.
student_1 = Student("Ayoub", 24)
student_2 = Student("Ayoub", 24)

print(student_1 == student_2)


# Les attributs sans valeur par défaut doivent être placés avant ceux ayant une valeur par défaut.

