"""empty message

Revision ID: 898486371de1
Revises: 080f7a08cf3a
Create Date: 2019-03-01 03:23:56.351405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '898486371de1'
down_revision = '080f7a08cf3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
