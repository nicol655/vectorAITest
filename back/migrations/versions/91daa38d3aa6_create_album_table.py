"""Create album table

Revision ID: 91daa38d3aa6
Revises: 
Create Date: 2020-11-01 23:02:21.469534

"""
from alembic import op
from sqlalchemy.sql import table
from sqlalchemy import String, Integer, Column


# revision identifiers, used by Alembic.
revision = '91daa38d3aa6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    album_table = op.create_table('album',
        Column("id", Integer, primary_key=True),
        Column("type", String),
        Column("title", String),
        Column("position", Integer),
        Column("img_src", String),
    )
    op.bulk_insert(album_table, [
        { 
            "id": 1,
            "type": "bank-draft",
            "title": "Bank Draft",
            "position": 0,
            "img_src": "https://cdn.pixabay.com/photo/2015/03/27/13/16/cat-694730_960_720.jpg",
        },
        { 
            "id": 2,
            "type": "bill-of-lading",
            "title": "Bill of Lading",
            "position": 1,
            "img_src": "https://cdn.pixabay.com/photo/2020/03/28/15/20/cat-4977436_960_720.jpg",
        },
        {
            "id": 3,
            "type": "invoice",
            "title": "Invoice",
            "position": 2,
            "img_src": "https://cdn.pixabay.com/photo/2020/10/04/04/24/cat-5625168_960_720.jpg",
        },
        {
            "id": 4,
            "type": "bank-draft-2",
            "title": "Bank Draft 2",
            "position": 3,
            "img_src": "https://cdn.pixabay.com/photo/2014/10/01/16/36/siamese-468814_960_720.jpg",
        },
        {
            "id": 5,
            "type": "bill-of-lading-2",
            "title": "Bill of Lading 2",
            "position": 4,
            "img_src": "https://cdn.pixabay.com/photo/2019/05/06/21/09/cat-4184276_960_720.jpg",
        }
    ])

def downgrade():
    op.drop_table('album')