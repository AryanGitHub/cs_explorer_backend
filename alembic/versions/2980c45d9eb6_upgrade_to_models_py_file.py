"""upgrade to models.py file

Revision ID: 2980c45d9eb6
Revises: 30ee25bf5006
Create Date: 2024-11-26 21:55:41.359178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2980c45d9eb6'
down_revision: Union[str, None] = '30ee25bf5006'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('resources_post', 'http_link',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('resources_post', 'http_link',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###