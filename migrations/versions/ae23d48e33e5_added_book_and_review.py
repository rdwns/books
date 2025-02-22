"""added book and review

Revision ID: ae23d48e33e5
Revises: 82c44319de4c
Create Date: 2020-05-02 21:41:38.026659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae23d48e33e5'
down_revision = '82c44319de4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('isbn', sa.String(length=64), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('author', sa.String(length=120), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('isbn')
    )
    op.create_index(op.f('ix_book_author'), 'book', ['author'], unique=True)
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=False)
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('isbn', sa.String(), nullable=True),
    sa.Column('review', sa.String(length=240), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['isbn'], ['book.isbn'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_review_isbn'), 'review', ['isbn'], unique=False)
    op.create_index(op.f('ix_review_uid'), 'review', ['uid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_review_uid'), table_name='review')
    op.drop_index(op.f('ix_review_isbn'), table_name='review')
    op.drop_table('review')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_index(op.f('ix_book_author'), table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###
