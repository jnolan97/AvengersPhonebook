"""added new model

Revision ID: d4f92a5ec8e9
Revises: 
Create Date: 2020-06-04 22:19:17.661149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4f92a5ec8e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usernamephone_number', sa.String(length=150), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('usernamephone_number')
    )
    op.create_table('phone_number',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('phone_numb', sa.String(length=50), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('phone_number')
    op.drop_table('user')
    # ### end Alembic commands ###