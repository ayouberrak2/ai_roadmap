class User:
    def __init__(
        self,
        name: str,
        email: str,
    ) -> None:
        self.name = name
        self._email = email

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if "@" not in value:
            raise ValueError("Adresse email invalide")

        self._email = value

    def display_information(self) -> None:
        print(f"Nom : {self.name}")
        print(f"Email : {self.email}")

    def describe_role(self) -> None:
        print("Rôle : utilisateur")


class Student(User):
    def __init__(
        self,
        name: str,
        email: str,
        course: str,
        daily_study_hours: int,
    ) -> None:
        super().__init__(name, email)

        self.course = course
        self.daily_study_hours = daily_study_hours

    def describe_role(self) -> None:
        print("Rôle : étudiant")

    def study(self) -> None:
        print(
            f"{self.name} étudie {self.course} "
            f"{self.daily_study_hours} heures par jour."
        )


class Trainer(User):
    def __init__(
        self,
        name: str,
        email: str,
        specialty: str,
    ) -> None:
        super().__init__(name, email)
        self.specialty = specialty

    def describe_role(self) -> None:
        print("Rôle : formateur")

    def teach(self) -> None:
        print(
            f"{self.name} enseigne {self.specialty}."
        )


users: list[User] = [
    Student(
        name="Ayoub",
        email="ayoub@example.com",
        course="Développement IA",
        daily_study_hours=8,
    ),
    Trainer(
        name="Sara",
        email="sara@example.com",
        specialty="Machine Learning",
    ),
]


for user in users:
    print("\n--- Utilisateur ---")

    user.display_information()
    user.describe_role()

    if isinstance(user, Student):
        user.study()

    elif isinstance(user, Trainer):
        user.teach()