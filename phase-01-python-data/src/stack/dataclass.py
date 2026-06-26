# ==================
#  dataclasses
# ===============

# DTO ;
# configuration ;
# résultat de calcul ;
# objet valeur ;
# structure de données ;
# données lues depuis un fichier ;
# résultat d’une requête.


# Une dataclass est une classe conçue principalement pour stocker des données.

from dataclasses import asdict, astuple, dataclass, field

@dataclass
class Consumption:
    unit_name:str
    electricity:float
    water :float
    # on peut faire @property dans dataclass

    @property
    def total_cost_exemple(self)->float:
        return self.electricity * self.water

    def __post_init__(self)->None:
        if not self.unit_name.strip():
            raise ValueError("le non est vide")

        if self.electricity<0:
            raise ValueError("la consomation de electricite doit etre positive")

        if self.water<0:
            raise ValueError("la consomation de eau doit etre positives ")

    def calculate_cost(self) -> float:
        return self.electricity * self.water

# La dataclass a automatiquement généré le constructeur.

consumption = Consumption(
    unit_name="Unité Safi",
    electricity=850,
    water=300,
)
con = asdict(consumption)
# Permet d’afficher clairement l’objet :
print(con)


@dataclass
class Student:
    name: str
    age: int
    courses: list[str] = field(default_factory=list) #Chaque étudiant possède sa propre liste.

# default_factory crée une nouvelle valeur pour chaque objet.


# Permet de comparer deux objets selon leurs valeurs.
student_1 = Student("Ayoub", 24)
student_2 = Student("Ayoub", 24)

# print(student_1 == student_2)


# Les attributs sans valeur par défaut doivent être placés avant ceux ayant une valeur par défaut.



# =========
# frozen
# ========

# Pourquoi utiliser frozen=True ?

# C’est utile pour représenter une valeur qui ne doit pas changer :

# coordonnées ;
# référence d’un verset ;
# identifiant ;
# période ;
# adresse ;
# configuration fixe ;
# objet valeur dans une architecture DDD.


@dataclass(frozen=True)
class Student:
    name: str
    age : int
    note : list[float] # on ne peut pas renplacer la liste mais on peut modidifier la liste (non parfais pour la securite)
    courses: tuple[str, ...] # parfais car tuple ne peut pas la modifier

student = Student(
    name="ayoubb",
    age=21,
    note=[12, 14, 16],
    courses=("Python", "Data"),
)

print(student.name)
# student.age = 21 # provoque FrozenInstanceError



# ===========
# slots
# ==========

# slots=True limite les attributs aux champs déclarés.

@dataclass(slots=True)
class Consumption:
    unit_name: str
    value: float

connn = Consumption(
    unit_name="pp1",
    value=93.2
)

# connn.exemple = "false exemple" #cause une error , car exemple n'ai pas declarer

# ====================================
# combiner frozen=True et slots=True
# ====================================

# possède uniquement les attributs déclarés ;
# ne peut pas être modifié ;
# compare ses valeurs automatiquement ;
# s’affiche correctement.

@dataclass(frozen=True, slots=True)
class AyahReference:
    surah_number: int
    ayah_number: int



# ==============================
#  comparaisan entre dataclass
# ==============================

student_1 = Student("Ayoub", 24, [12, 14], ("Python",))
student_2 = Student("Ayoub", 24, [12, 14], ("Python",))
student_3 = Student("Amine", 24, [10, 13], ("Data",))

print(student_1 == student_2) # True
print(student_1 == student_3) # False


# ========
#  trie
# ========

@dataclass(order=True)
class Product:
    price: float
    name: str  = field(compare=False) # il exclut le champ de la comparaison ( si 2 price est egaux dont les objet est egaux )

# La comparaison commence par le premier attribut (price) , si price est egaux en compare l'abribut prochaine (name)

product_1 = Product(100, "Livre")
product_2 = Product(150, "Clavier")

print(product_1 < product_2) # False


# trie avec sort
products = [
    Product(150, "Clavier"),
    Product(50, "Livre"),
    Product(100, "Souris"),
]

products.sort()

for product in products:
    print(product)



# ======================================
# Masquer un champ dans l’affichage
# ======================================

@dataclass
class User:
    username: str
    password_hash: str = field(repr=False)


user = User(
    username="ayoub",
    password_hash="hfrhiufhrihfiu",
)

# password_hash existe toujours, mais il n’apparaît pas dans l’affichage.

print(user) # resulta : User(username='ayoub')



# ===================
# asdict() , astuple
# ==================

# préparer des données ;
# créer du JSON ;
# envoyer une réponse API ;
# enregistrer dans un fichier ;
# transformer vers Pandas.


user = User(
    username="ayoub",
    password_hash="hfrhiufhrihfiu",
)

dict_user = asdict(user) #avec import
tuple_user = astuple(user) # avec import

print(dict_user)

# dict
# {
#     'username': 'ayoub',
# }

# tuple
# ('ayoub')

# =================================
# Héritage avec les dataclasses
# =================================

@dataclass
class Person:
    name: str
    age: int


@dataclass
class Student(Person):
    course: str

student = Student(
    name="Ayoub",
    age=24,
    course="Intelligence artificielle",
)

print(student)



# DTO ;
# configuration ;
# résultat de calcul ;
# objet valeur ;
# structure de données ;
# données lues depuis un fichier ;
# résultat d’une requête.

# Utilise plutôt une classe normale lorsque :

# elle possède beaucoup de logique métier ;
# elle contrôle fortement son état ;
# elle contient beaucoup de comportements ;
# sa construction est complexe ;
# son identité est plus importante que ses valeurs.
