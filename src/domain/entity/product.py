from dataclasses import dataclass

@dataclass
class Product:
    id: str
    name: str
    price: float

    def validate(self):
        if self.price <= 0:
            raise ValueError("Price must be greater than 0")
        if not self.name:
            raise ValueError("Name cannot be empty")
        if not self.id:
            raise ValueError("ID cannot be empty")
        
    def __post_init__(self):
        self.validate()