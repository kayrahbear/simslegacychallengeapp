"""empty message

Revision ID: 5463dcf74e02
Revises: 2d53885761d1
Create Date: 2023-03-20 00:21:22.364759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5463dcf74e02'
down_revision = '2d53885761d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aspiration',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('icon_url', sa.String(length=50), nullable=True),
    sa.Column('aspiration_type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('career',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('legacy_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skill',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('legacy_family_member',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('legacy_family', sa.Integer(), nullable=True),
    sa.Column('birth_status', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=50), nullable=True),
    sa.Column('age', sa.String(length=50), nullable=True),
    sa.Column('species', sa.String(length=50), nullable=True),
    sa.Column('infant_trait', sa.Integer(), nullable=True),
    sa.Column('toddler_trait', sa.Integer(), nullable=True),
    sa.Column('child_trait', sa.Integer(), nullable=True),
    sa.Column('teen_trait', sa.Integer(), nullable=True),
    sa.Column('ya_trait', sa.Integer(), nullable=True),
    sa.Column('child_aspiration', sa.Integer(), nullable=True),
    sa.Column('teen_aspiration', sa.Integer(), nullable=True),
    sa.Column('ya_aspiration', sa.Integer(), nullable=True),
    sa.Column('adult_aspiration', sa.Integer(), nullable=True),
    sa.Column('university_attended', sa.String(length=50), nullable=True),
    sa.Column('university_major', sa.String(length=50), nullable=True),
    sa.Column('parent_1', sa.Integer(), nullable=True),
    sa.Column('parent_2', sa.Integer(), nullable=True),
    sa.Column('spouse', sa.Integer(), nullable=True),
    sa.Column('legacy_role', sa.Integer(), nullable=True),
    sa.Column('in_household', sa.Boolean(), nullable=False),
    sa.Column('is_dead', sa.Boolean(), nullable=False),
    sa.Column('death_caused_by', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['adult_aspiration'], ['aspiration.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['child_aspiration'], ['aspiration.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['child_trait'], ['trait.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['infant_trait'], ['trait.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['legacy_family'], ['legacy_family.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['legacy_role'], ['legacy_role.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['parent_1'], ['legacy_family_member.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['parent_2'], ['legacy_family_member.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['spouse'], ['legacy_family_member.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['teen_aspiration'], ['aspiration.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['teen_trait'], ['trait.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['toddler_trait'], ['trait.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ya_aspiration'], ['aspiration.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ya_trait'], ['trait.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member_career',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('career_id', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['career_id'], ['career.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['legacy_family_member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member_skill',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('skill_id', sa.Integer(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['legacy_family_member.id'], ),
    sa.ForeignKeyConstraint(['skill_id'], ['skill.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member_skill')
    op.drop_table('member_career')
    op.drop_table('legacy_family_member')
    op.drop_table('skill')
    op.drop_table('legacy_role')
    op.drop_table('career')
    op.drop_table('aspiration')
    # ### end Alembic commands ###
