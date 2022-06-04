from typing import List, Union

from pydantic import BaseModel


class Player(BaseModel):
    id_player : int
    player_name : str
    minutes_played : int
    match_played : int
    goals : int
    assists : int
    saved : Union[int, None] = None
    conceded : Union[int, None] = None

    class Config:
        orm_mode = True


class Club(BaseModel):
    id_club: int
    club: str
    players: List[Player] = []

    class Config:
        orm_mode = True


class Position(BaseModel):
    id_position: int
    position: str
    players: List[Player] = []

    class Config:
        orm_mode = True