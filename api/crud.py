from sqlalchemy.orm import Session

import models


def get_players(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Player).order_by(models.Player.player_name).offset(skip).limit(limit).all()


def get_player_by_id(db: Session, id: int):
    return db.query(models.Player).filter(models.Player.id_player == id).first()


def get_clubs(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Club).offset(skip).limit(limit).all()


def get_positions(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Position).offset(skip).limit(limit).all()