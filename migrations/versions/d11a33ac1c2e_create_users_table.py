"""create users table

Revision ID: d11a33ac1c2e
Revises: ce7e5c3e6578
Create Date: 2022-11-14 22:54:35.669649

"""
from alembic import op
import sqlalchemy as sa

from werkzeug.security import generate_password_hash
import datetime

# revision identifiers, used by Alembic.
revision = 'd11a33ac1c2e'
down_revision = 'ce7e5c3e6578'
branch_labels = None
depends_on = None


def upgrade() -> None:
    first_user = op.create_table(
        'User',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('firstname', sa.String),
        sa.Column('lastname', sa.String),
        sa.Column('email', sa.String),
        sa.Column('password_hash', sa.String),
    )
    op.bulk_insert(
        first_user,
        [
            {'firstname': 'Test', "lastname": "Test", "email": "test@gmail.com", "password_hash": generate_password_hash("1234", method='sha256')},
        ]
    )


def downgrade() -> None:
    op.drop_table('account')
