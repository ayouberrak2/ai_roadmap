# ============================
# Object-Oriented Programming
# ============================




class Perssone :
    def __init__ (
        self,
        name : str,
        age :int,
        is_student : bool,
        note : list[int]
    )->None:
        self.name = name,
        self.age = age,
        self.is_student = is_student
        self.note = note


    def afficher_info(
            self
    )->str:
        if self.is_student == True:
            print(f"mon non est : {self.name} et mon age est : {self.age} et je suis un etudiant")
        else :
            print(f"mon non est : {self.name} et mon age est : {self.age} et je ne suis pas un etudiant")

    # getter and setter
    # ===================

    def get_name(self)->str:
        return self.name

    def set_name(self , name:str)->None:
        self.name = name

    # =====================


per1 = Perssone(
    name="ayoub",
    age=21,
    is_student=True,
    note=[12,3,2,1,2]
)


list_personne = [
    Perssone(name="ahmed",age=22,is_student=True ,note=[12,3,2,1,2]),
    Perssone(name="mohamed",age=24,is_student=False,note=[12,3,2,1,2]),
    Perssone(name="mazine",age=25,is_student=True,note=[12,3,2,1,2])
]
per1.afficher_info();









# ===========================
# L’encapsulation
# ======================

# self.name = name public
# self.__name = name private
# self._name = name protected

# =========
# public ==
# =========

# Lorsque la valeur ne nécessite pas de validation ou de protection particulière.

# =========
# private ==
# =========

# “cet élément appartient à cette classe,
# ne l’utilise pas directement,
# et évite de le remplacer accidentellement dans une sous-classe”

# self.__name ; ==> devient print(_ClassName__name)

# =========
# protected
# =========
# L’accès extérieur est interdit.



# ==============
# @property
# ================

# @property permet d’utiliser une méthode comme si elle était un attribut.


class Produit :
    def __init__(self,price:int)->None:
        # self._price = price;
        # Pour appliquer la validation dès la création, utilise la propriété dans le constructeur :
        self.price = price;


    @property # getter
    def price(self)->float:
        return self._price

    @price.setter   #setter
    def price(self,new_price:int)-> None:
        self._price = new_price


product = Produit(100)

# ustilisation de getter
print(product.price)

# utilisation de setter
product.price = 150


# Python appelle en réalité automatiquement la méthode :
# print(product.price())

# Une propriété ne doit pas forcément correspondre à une valeur stockée.
# on peut faire un property(getter) sans setter 

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height


# Deleter avec @property
# @email.deleter
# def email(self) -> None:
#     print("Suppression de l'adresse email")
#     del self._email
