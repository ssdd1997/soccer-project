from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Club(Base):
    __tablename__ = 't_clubs'
    id_club = Column(Integer, primary_key=True)
    club = Column(String)
    players = relationship("Player", back_populates="club")


class Position(Base):
    __tablename__ = 't_positions'
    id_position = Column(Integer, primary_key=True)
    position = Column(String)
    players = relationship("Player", back_populates="position")


class Player(Base):
    __tablename__ = "t_players"

    id_player = Column(Integer, primary_key=True, index=True)
    player_name = Column(String)
    minutes_played = Column(Integer)
    match_played = Column(Integer)
    goals = Column(Integer)
    assists = Column(Integer)
    saved = Column(Integer)
    conceded = Column(Integer)
    fk_club = Column(Integer, ForeignKey("t_clubs.id_club"))
    fk_position = Column(Integer, ForeignKey("t_positions.id_position"))

    club = relationship("Club", back_populates="players")
    position = relationship("Position", back_populates="players")