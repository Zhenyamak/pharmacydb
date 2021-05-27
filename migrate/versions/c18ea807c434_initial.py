"""initial

Revision ID: c18ea807c434
Revises: 
Create Date: 2021-05-24 13:11:34.794500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c18ea807c434'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('age', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('component',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('medicine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('storage_time', sa.Date(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('type', sa.Enum('pill', 'ointment', 'tincture', 'mixture', 'liquor', 'powder', name='medicinetype'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('cooking_book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medicine_id', sa.Integer(), nullable=True),
    sa.Column('method', sa.Enum('mixing', 'creaming', name='cookingmethod'), nullable=True),
    sa.ForeignKeyConstraint(['medicine_id'], ['medicine.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('critical_norm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('component_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['component_id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('component_id', sa.Integer(), nullable=True),
    sa.Column('dose', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['component_id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('in_process', 'waiting_for_components', 'ready', 'closed', name='orderstatus'), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('medicine_id', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['medicine_id'], ['medicine.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supply_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('component_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['component_id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ingredient_medicine',
    sa.Column('ingredient_id', sa.Integer(), nullable=True),
    sa.Column('medicine_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], ),
    sa.ForeignKeyConstraint(['medicine_id'], ['medicine.id'], )
    )
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medicine_name', sa.String(length=120), nullable=True),
    sa.Column('doctor', sa.String(length=255), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('diagnosis', sa.String(length=255), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('consumption_type', sa.Enum('internal', 'external', 'mixing', name='consumptiontype'), nullable=True),
    sa.Column('ready_time', sa.Date(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe')
    op.drop_table('ingredient_medicine')
    op.drop_table('supply_request')
    op.drop_table('orders')
    op.drop_table('ingredient')
    op.drop_table('critical_norm')
    op.drop_table('cooking_book')
    op.drop_table('medicine')
    op.drop_table('component')
    op.drop_table('client')
    # ### end Alembic commands ###
