"""empty message

Revision ID: e841b6598df0
Revises: 
Create Date: 2024-03-14 08:31:14.716184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e841b6598df0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('test_id', sa.Integer(), nullable=False),
    sa.Column('appointment_date', sa.String(length=50), nullable=False),
    sa.Column('status', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('patient_id'),
    sa.UniqueConstraint('status')
    )
    op.create_table('patientProfile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_of_birth', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('testResults',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('test_id', sa.Integer(), nullable=False),
    sa.Column('date_taken', sa.String(length=50), nullable=False),
    sa.Column('result_pdf_path', sa.String(length=256), nullable=False),
    sa.Column('status', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('patient_id'),
    sa.UniqueConstraint('status')
    )
    op.create_table('tests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('test_name', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('recommended_interval', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('test_name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('user_role', sa.String(length=50), nullable=False),
    sa.Column('registration_date', sa.Date(), nullable=False),
    sa.Column('user_email', sa.String(length=70), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('tests')
    op.drop_table('testResults')
    op.drop_table('patientProfile')
    op.drop_table('appointments')
    # ### end Alembic commands ###
