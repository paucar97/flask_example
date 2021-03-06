"""empty message

Revision ID: 459562328214
Revises: 
Create Date: 2020-04-11 11:49:33.598422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '459562328214'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ALUMNO_DB',
    sa.Column('ID_ALUMNO', sa.Integer(), nullable=False),
    sa.Column('NOMBRE', sa.String(length=50), nullable=False),
    sa.Column('APELLIDO_PATERNO', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('ID_ALUMNO')
    )
    op.create_table('CURSO_DB',
    sa.Column('ID_CURSO', sa.Integer(), nullable=False),
    sa.Column('NOMBRE_CURSO', sa.String(length=50), nullable=False),
    sa.Column('CREDITO', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ID_CURSO')
    )
    op.create_table('ALUMNO_X_CURSO_DB',
    sa.Column('ID_CURSO', sa.Integer(), nullable=False),
    sa.Column('ID_ALUMNO', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ID_ALUMNO'], ['ALUMNO_DB.ID_ALUMNO'], ),
    sa.ForeignKeyConstraint(['ID_CURSO'], ['CURSO_DB.ID_CURSO'], ),
    sa.PrimaryKeyConstraint('ID_CURSO', 'ID_ALUMNO')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ALUMNO_X_CURSO_DB')
    op.drop_table('CURSO_DB')
    op.drop_table('ALUMNO_DB')
    # ### end Alembic commands ###
