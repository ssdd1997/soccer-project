from sqlalchemy.orm import Session

import models


def get_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Player).offset(skip).limit(limit).all()


def get_clubs(db: Session, skip: int = 0, limit: int = 1):
    return db.query(models.Club).offset(skip).limit(limit).all()


def get_positions(db: Session, skip: int = 0, limit: int = 1):
    return db.query(models.Position).offset(skip).limit(limit).all()