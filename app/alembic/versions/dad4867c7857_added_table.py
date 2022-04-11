"""Added table

Revision ID: dad4867c7857
Revises: 
Create Date: 2022-04-11 15:28:49.761282

"""
from alembic import op
import sqlalchemy as sa
import common.guid_type


# revision identifiers, used by Alembic.
revision = 'dad4867c7857'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rules',
    sa.Column('id', common.guid_type.GUID(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', common.guid_type.GUID(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('mobile', sa.Integer(), nullable=False),
    sa.Column('team', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('rule_id', common.guid_type.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['rule_id'], ['rules.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('worklogs',
    sa.Column('id', common.guid_type.GUID(), nullable=False),
    sa.Column('user_id', common.guid_type.GUID(), nullable=False),
    sa.Column('timestamp_in', sa.DateTime(), nullable=False),
    sa.Column('timestamp_out', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_worklogs_id'), 'worklogs', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_worklogs_id'), table_name='worklogs')
    op.drop_table('worklogs')
    op.drop_table('users')
    op.drop_table('rules')
    # ### end Alembic commands ###