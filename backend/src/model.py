from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import BigInteger, Boolean, Integer, SmallInteger, Text
from .db import Base


class User(Base):
    __tablename__ = "user"

    id = Column("id", BigInteger, primary_key=True)
    name = Column("name", Text, nullable=False, unique=True)
    password = Column("password", Text, nullable=False)


class Action(Base):
    __tablename__ = "action"

    id = Column("id", BigInteger, primary_key=True)
    severity_id = Column(SmallInteger, ForeignKey("severity.id"))
    severity = relationship("Severity", back_populates="actions")
    content = Column("content", Text, nullable=False, unique=True)

    punishments = relationship("Punishment", back_populates="action")


class Severity(Base):
    __tablename__ = "severity"

    id = Column("id", SmallInteger, primary_key=True)
    level = Column("level", SmallInteger, nullable=False, unique=True)
    name = Column("name", Text, nullable=False, unique=True)

    actions = relationship("Action", back_populates="severity")


class Punishment(Base):
    __tablename__ = "punishment"

    id = Column("id", BigInteger, primary_key=True)

    action_id = Column(BigInteger, ForeignKey("action.id"))
    action = relationship("Action", back_populates="punishments")

    punishment_type_id = Column(SmallInteger, ForeignKey("punishment_type.id"))
    punishment_type = relationship(
        "PunishmentType",
        back_populates="punishments",
    )

    quantity = Column("quantity", Integer, nullable=False)


class AssignedPunishment(Base):
    __tablename__ = "assigned_punishment"

    id = Column("id", BigInteger, primary_key=True)
    active = Column("active", Boolean, default=True)

    punishment_id = Column(BigInteger, ForeignKey("punishment.id"))
    punishment = relationship("Punishment", back_populates="assigned")

    user_id = Column(BigInteger, ForeignKey("user.id"))
    user = relationship("User", back_populates="assigned_punishments")


class PunishmentType(Base):
    __tablename__ = "punishment_type"

    id = Column("id", SmallInteger, primary_key=True)
    name = Column("name", Text, nullable=False, unique=True)


# Re-import with tables included
meta = Base.metadata
