"""create uuid extension

Revision ID: 979c148da4aa
Revises: f0ecde9b331b
Create Date: 2022-05-27 20:00:39.657151

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "979c148da4aa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""CREATE EXTENSION IF NOT EXISTS "uuid-ossp";""")


def downgrade():
    pass
