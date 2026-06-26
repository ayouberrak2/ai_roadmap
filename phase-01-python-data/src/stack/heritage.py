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

