from dataclasses import dataclass

@dataclass
class Address:
    street: str
    city: str
    state: str
    zip_code: str
    country: str

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.street:
            raise ValueError("Street is required")
        if not self.city:
            raise ValueError("City is required")
        if not self.state:
            raise ValueError("State is required")
        if not self.zip_code:
            raise ValueError("Zip code is required")
        if not self.country:
            raise ValueError("Country is required")
        
    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}"