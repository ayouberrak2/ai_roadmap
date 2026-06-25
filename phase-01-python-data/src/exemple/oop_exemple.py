class EnergyUnit:
    def __init__(
        self,
        name: str,
        city: str,
        active: bool = True,
    ) -> None:
        self.name = name
        self.city = city
        self.active = active
        self.consumptions: list[float] = []

    def add_consumption(self, value: float) -> None:
        if value < 0:
            raise ValueError(
                "La consommation ne peut pas être négative"
            )

        self.consumptions.append(value)

    def calculate_total(self) -> float:
        return sum(self.consumptions)

    def calculate_average(self) -> float:
        if not self.consumptions:
            return 0.0

        return sum(self.consumptions) / len(
            self.consumptions
        )

    def has_high_consumption(self) -> bool:
        return self.calculate_average() > 1000

    def display_summary(self) -> None:
        print(f"Nom : {self.name}")
        print(f"Ville : {self.city}")
        print(f"Active : {self.active}")
        print(f"Total : {self.calculate_total():.2f} kWh")
        print(
            f"Moyenne : "
            f"{self.calculate_average():.2f} kWh"
        )


unit = EnergyUnit(
    name="Unité Marrakech",
    city="Marrakech",
)

unit.add_consumption(900)
unit.add_consumption(1200)
unit.add_consumption(1500)

unit.display_summary()

if unit.has_high_consumption():
    print("Alerte : consommation moyenne élevée")
