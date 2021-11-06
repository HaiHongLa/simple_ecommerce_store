"""empty message

Revision ID: 37a12a6d8308
Revises: 4be30f2fb087
Create Date: 2021-11-05 23:09:18.004807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37a12a6d8308'
down_revision = '4be30f2fb087'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('order_items')
    op.drop_table('order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('order_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('reference', sa.VARCHAR(length=5), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('country', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('payment_type', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='order_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('order_items',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name='order_items_order_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='order_items_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='order_items_pkey')
    )
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('stock', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='product_pkey'),
    sa.UniqueConstraint('name', name='product_name_key')
    )
    # ### end Alembic commands ###
