from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)


class Recipe(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True)
    ingredients: Mapped[str] = mapped_column(unique=True)
    instructions: Mapped[str] = mapped_column(unique=True)
    source: Mapped[str]
    addedAt: Mapped[str]

    def as_dict(self):
        return { r.name: getattr(self, r.name) for r in self.__table__.columns}
