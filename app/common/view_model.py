from pydantic import BaseModel

class ViewModel(BaseModel):
    class Config:
        orm_mode = True