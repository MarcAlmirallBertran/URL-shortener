"""init

Revision ID: 2bd5f6759a32
Revises: 
Create Date: 2023-12-03 13:48:23.129141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bd5f6759a32'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_urls_key', table_name='urls')
    op.drop_index('ix_urls_secret_key', table_name='urls')
    op.drop_index('ix_urls_target_url', table_name='urls')
    op.drop_table('urls')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('key', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('secret_key', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('target_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('clicks', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='urls_pkey')
    )
    op.create_index('ix_urls_target_url', 'urls', ['target_url'], unique=False)
    op.create_index('ix_urls_secret_key', 'urls', ['secret_key'], unique=False)
    op.create_index('ix_urls_key', 'urls', ['key'], unique=False)
    # ### end Alembic commands ###