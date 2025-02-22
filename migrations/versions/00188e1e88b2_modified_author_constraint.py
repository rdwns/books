"""modified author constraint

Revision ID: 00188e1e88b2
Revises: ae23d48e33e5
Create Date: 2020-05-22 20:55:07.486653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00188e1e88b2'
down_revision = 'ae23d48e33e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_book_author', table_name='book')
    op.create_index(op.f('ix_book_author'), 'book', ['author'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_book_author'), table_name='book')
    op.create_index('ix_book_author', 'book', ['author'], unique=1)
    # ### end Alembic commands ###
