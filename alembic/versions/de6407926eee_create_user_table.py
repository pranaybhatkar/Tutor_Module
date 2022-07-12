"""create_user_table

Revision ID: de6407926eee
Revises: 
Create Date: 2022-07-11 22:12:12.843482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de6407926eee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_type',
        sa.Column('user_name', sa.String(100), primary_key=True),
        sa.Column('birthdate', sa.String(20), nullable=False)
        # sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('user_type')
