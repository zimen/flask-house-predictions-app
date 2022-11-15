"""create prediction table

Revision ID: ce7e5c3e6578
Revises: 
Create Date: 2022-11-14 22:54:14.912098

"""
from alembic import op
import sqlalchemy as sa

import datetime 
# revision identifiers, used by Alembic.
revision = 'ce7e5c3e6578'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'Prediction',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('created_on', sa.DateTime, default=datetime.date.today()),
        sa.Column('overall_qual', sa.Integer),
        sa.Column('neighborhood', sa.String),
        sa.Column('year_remod_add', sa.Integer),
        sa.Column('exterior_1st', sa.String),
        sa.Column('bsmt_qual', sa.String),
        sa.Column('exter_qual', sa.String),
        sa.Column('kitchen_qual', sa.String),
        sa.Column('garage_qual', sa.String),
        sa.Column('fireplaces', sa.Integer),
        sa.Column('fireplace_qu', sa.String),
        sa.Column('full_bath', sa.Integer),
        sa.Column('half_bath', sa.Integer),
        sa.Column('bsmt_full_bath', sa.Integer),
        sa.Column('bsmt_half_bath', sa.Integer),
        sa.Column('utilities', sa.String),
        sa.Column('gr_liv_area', sa.Integer),
        sa.Column('total_bsmt_sf', sa.Integer),
        sa.Column('first_flr_sf', sa.Integer),
        sa.Column('second_flr_sf', sa.Integer),
        sa.Column('open_porch_sf', sa.Integer),
        sa.Column('wood_deck_sf', sa.Integer),
        sa.Column('pool_area', sa.Integer),
        sa.Column('heating_qc', sa.String),
        sa.Column('bsmt_exposure', sa.String),
        sa.Column('paved_drive', sa.String),
        sa.Column('street', sa.String),
        sa.Column('central_air', sa.String),
        sa.Column('condition_1', sa.String),
        sa.Column('condition_2', sa.String),
        sa.Column('garage_cars', sa.Integer),
        sa.Column('garage_finish', sa.String),
        sa.Column('garage_area', sa.Integer),
        sa.Column('sale_condition', sa.String),
        sa.Column('price', sa.Integer),
    )



def downgrade() -> None:
    op.drop_table('Prediction')
