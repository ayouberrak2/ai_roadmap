class User:
    def __init__(
        self,
        name: str,
        email: str,
    ) -> None:
        self.name = name
        self.email = email

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
    ) -> None:
        super().__init__(name, email)
        self.course = course

    def study(self) -> None:
        print(
            f"{self.name} étudie la formation "
            f"{self.course}."
        )

    def describe_role(self) -> None:
        print("Rôle : étudiant")


class Trainer(User):
    def __init__(
        self,
        name: str,
        email: str,
        specialty: str,
    ) -> None:
        super().__init__(name, email)
        self.specialty = specialty

    def teach(self) -> None:
        print(
            f"{self.name} enseigne "
            f"{self.specialty}."
        )

    def describe_role(self) -> None:
        print("Rôle : formateur")


student = Student(
    name="Ayoub",
    email="ayoub@example.com",
    course="Intelligence artificielle",
)

trainer = Trainer(
    name="Sara",
    email="sara@example.com",
    specialty="Machine Learning",
)

student.display_information()
student.describe_role()
student.study()

print()

trainer.display_information()
trainer.describe_role()
trainer.teach()
