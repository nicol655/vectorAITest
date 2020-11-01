"""Album model module."""
from settings import metadata, sqlalchemy

album = sqlalchemy.Table(
  "album",
  metadata,
  sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
  sqlalchemy.Column("type", sqlalchemy.String),
  sqlalchemy.Column("title", sqlalchemy.String),
  sqlalchemy.Column("position", sqlalchemy.Integer),
  sqlalchemy.Column("img_src", sqlalchemy.String),
)
