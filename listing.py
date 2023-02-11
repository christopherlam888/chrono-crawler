from dataclasses import dataclass


@dataclass(eq=True)
class Listing:
    title: str
    price: int
    photo: str
    url: str
    store: str

    def __lt__(self, other):
        return self.price <= other.price
