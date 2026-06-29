# ===================
# L’héritage
# =================


# L’héritage permet de créer une nouvelle classe à partir d’une classe existante.

# La nouvelle classe récupère :

# les attributs de la classe parente ;
# ses méthodes ;
# son comportement général.

# Elle peut ensuite :

# ajouter de nouveaux attributs ;
# # ajouter de nouvelles méthodes ;
# modifier les méthodes héritées.

# ========================
# sans heritage
# =====================

class Student:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def display_information(self) -> None:
        print(self.name)
        print(self.email)


class Trainer:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def display_information(self) -> None:
        print(self.name)
        print(self.email)


# =========================
# avec heritage
# ===========================
class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def display_information(self) -> None:
        print(f"Nom : {self.name}")
        print(f"Email : {self.email}")

    def describe_role(self) -> None:
        print("Je suis un utilisateur.")


class Student(User): # student herite de user

    def __init__(self,name:str,email:str,note:int)->None:
        super().__init__(name=name,email=email) # heritage de constructeur 
        self.note = note

    def study(self) -> None:
        print(f"{self.name} est en train d'étudier Python.")

    def display_information(self) -> None:
        super().display_information() # appler de methode parent 
        print("Rôle : étudiant")

    def describe_role(self) -> None: #override (polymorphisme redifinition )
        print("Je suis un etudiant.")


class Trainer(User):
    pass


# utilisation
student = Student(name="ayoub",email="ayouberrak@gmail.com", note=15)
student.display_information()



# ==================
# isinstance()
# ===============

# comme instanceof() dans php
# suposans quon a user et student herite de user
student = Student(name="ayoub", email="ayouberrak@gmail.com", note=15)

print(isinstance(student, Student)) # True

print(isinstance(student, User)) # aussi True


# issubclass() vérifie une relation entre deux classes
print(issubclass(Student, User)) # True


# ================================
# Héritage et attributs publics
# ================================


class User:
    def __init__(self, name: str) -> None:
        self.name = name

class Student(User):
    def display_name(self) -> None:
        print(self.name)


# ================================
# Héritage et attributs protégés
# ================================

class User:
    def __init__(self, email: str) -> None:
        self._email = email

class Student(User):
    def display_email(self) -> None:
        print(self._email)

# ========================
# Héritage et attributs privee
# ================================

class User:
    def __init__(self, password: str) -> None:
        self.__password = password


class Student(User):
    def display_password(self) -> None:
        print(self.__password) # error

#  car dans user passord se transfome a self._User__password et dans student il se transforma a self._Student__password

# bonne exemple :
class User:
    def __init__(self, password: str) -> None:
        self.__password = password

    def check_password(self, password: str) -> bool:
        return self.__password == password
    
class Student(User):
    def authenticate(self, password: str) -> None:
        if self.check_password(password):
            print("Mot de passe correct")
        else:
            print("Mot de passe incorrect")


# ===========================
# Chaîne d’héritage
# ==========================

class User:
    def login(self) -> None:
        print("Connexion")


class Employee(User):
    def work(self) -> None:
        print("Travail")


class Manager(Employee):
    def manage_team(self) -> None:
        print("Gestion de l'équipe")

manager = Manager() # est user et employe 

manager.login()
manager.work()
manager.manage_team()


# =============================
# Héritage multiple
# ======================
class Logger:
    def log(self, message: str) -> None:
        print(f"LOG : {message}")


class Serializable:
    def serialize(self) -> str:
        return "Objet sérialisé"


class User(Logger, Serializable):
    pass


user = User()

user.log("Utilisateur créé")
print(user.serialize())



# Problème !!!!!!!!!!!!!!!!!!!!!
# exemple
class ParentA:
    def display(self) -> None:
        print("Parent A")


class ParentB:
    def display(self) -> None:
        print("Parent B")


class Child(ParentA, ParentB):
    pass


child = Child()
child.display() # cette method de class Parent a

# Python suit un ordre appelé : MRO — Method Resolution Order

print(Child.mro()) 

# result :
# Child
# ParentA
# ParentB
# object

# ====================
# Classes abstraites
# =======================

from abc import ABC , abstractmethod

class PredictionModel(ABC):
    @abstractmethod
    def predict(self, value: float) -> float:
        pass

class LinearModel(PredictionModel):
    def predict(self, value: float) -> float:
        return value * 2
    
model = LinearModel()

print(model.predict(10))

model = PredictionModel() #error

