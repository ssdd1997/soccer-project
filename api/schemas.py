from typing import List

from pydantic import BaseModel


class Player(BaseModel):
    goals: int

    class Config:
        orm_mode = True


class Club(BaseModel):
    id_club: int
    club: str
    players: List[Player] = []

    class Config:
        orm_mode = True


class Position(BaseModel):
    is_position: int
    position: str
    players: List[Player] = []

    class Config:
        orm_mode = True