"""Create album table

Revision ID: 91daa38d3aa6
Revises: 
Create Date: 2020-11-01 23:02:21.469534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91daa38d3aa6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'album',
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("type", sa.String),
        sa.Column("title", sa.String),
        sa.Column("position", sa.Integer),
        sa.Column("img_src", sa.String),
    )

def downgrade():
    op.drop_table('album')