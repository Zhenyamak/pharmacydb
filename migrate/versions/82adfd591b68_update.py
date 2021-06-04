"""update

Revision ID: 82adfd591b68
Revises: 0d7476ad279c
Create Date: 2021-06-04 18:27:18.335651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82adfd591b68'
down_revision = '0d7476ad279c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('cooking_book_ibfk_1', 'cooking_book', type_='foreignkey')
    op.create_foreign_key(None, 'cooking_book', 'medicine', ['medicine_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('ingredient_medicine_ibfk_2', 'ingredient_medicine', type_='foreignkey')
    op.create_foreign_key(None, 'ingredient_medicine', 'medicine', ['medicine_id'], ['id'], ondelete='CASCADE')
    op.add_column('orders', sa.Column('ready_time', sa.Date(), nullable=True))
    op.drop_constraint('orders_ibfk_2', 'orders', type_='foreignkey')
    op.drop_constraint('orders_ibfk_1', 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'medicine', ['medicine_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'orders', 'client', ['client_id'], ['id'], ondelete='CASCADE')
    op.drop_column('recipe', 'ready_time')
    op.drop_constraint('supply_request_ibfk_1', 'supply_request', type_='foreignkey')
    op.create_foreign_key(None, 'supply_request', 'client', ['client_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'supply_request', type_='foreignkey')
    op.create_foreign_key('supply_request_ibfk_1', 'supply_request', 'client', ['client_id'], ['id'])
    op.add_column('recipe', sa.Column('ready_time', sa.DATE(), nullable=True))
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key('orders_ibfk_1', 'orders', 'client', ['client_id'], ['id'])
    op.create_foreign_key('orders_ibfk_2', 'orders', 'medicine', ['medicine_id'], ['id'])
    op.drop_column('orders', 'ready_time')
    op.drop_constraint(None, 'ingredient_medicine', type_='foreignkey')
    op.create_foreign_key('ingredient_medicine_ibfk_2', 'ingredient_medicine', 'medicine', ['medicine_id'], ['id'])
    op.drop_constraint(None, 'cooking_book', type_='foreignkey')
    op.create_foreign_key('cooking_book_ibfk_1', 'cooking_book', 'medicine', ['medicine_id'], ['id'])
    # ### end Alembic commands ###
