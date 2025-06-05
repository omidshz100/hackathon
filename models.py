from pydantic import BaseModel

class Lawyer(BaseModel):
    id: int
    name: str
    specialty: str
    city: str
    contact: str