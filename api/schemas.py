from typing import List, Union, Optional

from pydantic import BaseModel


class ClubBase(BaseModel):
    club: str


class PositionBase(BaseModel):
    position: str


class PlayerBase(BaseModel):
    player_name: str
    minutes_played: int
    match_played: int
    goals: int
    assists: int
    saved: Union[int, None] = None
    conceded: Union[int, None] = None
    fk_club: int
    fk_position: int


class Player(PlayerBase):
    id_player: int

    class Config:
        orm_mode = True


class Club(ClubBase):
    id_club: int

    class Config:
        orm_mode = True


class Position(PositionBase):
    id_position: int

    class Config:
        orm_mode = True


class PlayerWithClubAndPosition(Player):
    club: Club
    position: Position


class ClubWithPlayers(Club):
    players: List[Player]


class PositionWithPlayers(Position):
    players: List[Player]


