"""empty message

Revision ID: 5f0930171396
Revises: 
Create Date: 2021-03-04 11:33:29.049440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f0930171396'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('co_op_job',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('job_title', sa.String(length=255), nullable=True),
    sa.Column('job_description', sa.String(length=255), nullable=True),
    sa.Column('vacancy', sa.Integer(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('details', sa.String(length=255), nullable=True),
    sa.Column('intention', sa.String(length=255), nullable=True),
    sa.Column('remote', sa.Boolean(), nullable=True),
    sa.Column('alumni', sa.Boolean(), nullable=True),
    sa.Column('hourly_rate', sa.Float(), nullable=True),
    sa.Column('expires_on', sa.DateTime(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('co_op_job')
    # ### end Alembic commands ###
