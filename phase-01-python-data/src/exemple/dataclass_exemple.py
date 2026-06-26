from dataclasses import asdict, dataclass, field


@dataclass(slots=True)
class Consumption:
    unit_name: str
    electricity_kwh: float
    water_m3: float
    price_per_kwh: float = 1.25
    alerts: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.unit_name = self.unit_name.strip()

        if not self.unit_name:
            raise ValueError(
                "Le nom de l'unité est obligatoire"
            )

        if self.electricity_kwh < 0:
            raise ValueError(
                "La consommation électrique "
                "ne peut pas être négative"
            )

        if self.water_m3 < 0:
            raise ValueError(
                "La consommation d'eau "
                "ne peut pas être négative"
            )

        if self.price_per_kwh < 0:
            raise ValueError(
                "Le prix ne peut pas être négatif"
            )

        if self.electricity_kwh > 1000:
            self.alerts.append(
                "Consommation électrique élevée"
            )

    @property
    def electricity_cost(self) -> float:
        return self.electricity_kwh * self.price_per_kwh

    @property
    def consumption_level(self) -> str:
        if self.electricity_kwh > 1500:
            return "critique"

        if self.electricity_kwh > 1000:
            return "élevée"

        if self.electricity_kwh > 500:
            return "moyenne"

        return "faible"


consumption = Consumption(
    unit_name="Unité Safi",
    electricity_kwh=1250,
    water_m3=300,
)

print(consumption)

print(
    f"Coût électrique : "
    f"{consumption.electricity_cost:.2f} DH"
)

print(
    f"Niveau : {consumption.consumption_level}"
)

print(f"Alertes : {consumption.alerts}")

consumption_data = asdict(consumption)

print(consumption_data)
