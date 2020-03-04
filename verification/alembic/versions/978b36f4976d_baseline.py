"""baseline

Revision ID: 978b36f4976d
Revises: 
Create Date: 2020-03-03 16:28:58.660139

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '978b36f4976d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jumio_verification',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('verification_id', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('jumio_reference_id', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('user_reference_id', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('redirect_url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('transaction_status', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('verification_status', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('transaction_date', mysql.TIMESTAMP(), nullable=True),
    sa.Column('callback_date', mysql.TIMESTAMP(), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('verification',
    sa.Column('id', mysql.VARCHAR(length=225), nullable=False),
    sa.Column('verification_type', mysql.VARCHAR(length=225), nullable=False),
    sa.Column('entity_id', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('status', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('requestee', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', mysql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'verification_type')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('verification')
    op.drop_table('jumio_verification')
    # ### end Alembic commands ###
