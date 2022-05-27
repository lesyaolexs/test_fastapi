"""Add users

Revision ID: f0ecde9b331b
Revises: c255a00ed374
Create Date: 2022-05-27 19:32:32.905520

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "f0ecde9b331b"
down_revision = "c255a00ed374"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
    INSERT INTO "user"(first_name, last_name, birthday, id)
VALUES ('l', 'o', '2022-05-19', 'bfde8bae-5b25-495e-9e87-37ab1695f5ae'),
       ('s', 'h', '2022-05-11', 'f2c4fd81-c756-4a1c-af0c-222316828afe'),
       ('m', 'l', null, 'f93b6a00-945c-4394-88e2-80d6e9335d95')"""
    )


def downgrade():
    pass
