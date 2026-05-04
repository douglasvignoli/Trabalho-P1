"""create animals table

Revision ID: a1b2c3d4e5f6
Revises:
Create Date: 2026-05-04 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'animals',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(), nullable=False),
        sa.Column('especie', sa.String(), nullable=False),
        sa.Column('raca', sa.String(), nullable=False),
        sa.Column('idade', sa.Integer(), nullable=False),
        sa.Column('peso', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_animals_id'), 'animals', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_animals_id'), table_name='animals')
    op.drop_table('animals')
