class EnergyUnit:
    def __init__(
        self,
        name: str,
        consumption: float,
    ) -> None:
        self.name = name
        self.consumption = consumption

    @property
    def consumption(self) -> float:
        return self._consumption

    @consumption.setter
    def consumption(self, new_value: float) -> None:
        if not isinstance(new_value, int | float):
            raise TypeError(
                "La consommation doit être un nombre"
            )

        if new_value < 0:
            raise ValueError(
                "La consommation ne peut pas être négative"
            )

        self._consumption = float(new_value)

    @property
    def level(self) -> str:
        if self._consumption > 1500:
            return "critique"

        if self._consumption > 1000:
            return "élevée"

        if self._consumption > 500:
            return "moyenne"

        return "faible"



unit = EnergyUnit(
    name="Unité Safi",
    consumption=850,
)

print(unit.name)
print(unit.consumption)
print(unit.level)

unit.consumption = 1700

print(unit.level)
