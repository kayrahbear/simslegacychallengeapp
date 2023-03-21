"""create starting_law and trait tables

Revision ID: 36642820b265
Revises: 74ceec13bc4c
Create Date: 2023-03-20 00:12:32.250905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36642820b265'
down_revision = '74ceec13bc4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('starting_law',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('law_type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trait',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=350), nullable=True),
    sa.Column('icon_url', sa.String(length=50), nullable=True),
    sa.Column('trait_type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trait')
    op.drop_table('starting_law')
    # ### end Alembic commands ###
