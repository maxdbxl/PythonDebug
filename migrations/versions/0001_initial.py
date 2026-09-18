from alembic import op
import sqlalchemy as sa


revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('createdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updatedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deletedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.Column('userid', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=50), nullable=False),
        sa.Column('useremail', sa.String(length=100), nullable=False),
        sa.Column('userpassword', sa.String(length=100), nullable=False),
        sa.Column('userdescription', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('userid')
    )
    op.create_index(op.f('ix_users_useremail'), 'users', ['useremail'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)

    op.create_table('roles',
        sa.Column('createdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updatedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deletedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.Column('roleid', sa.Integer(), nullable=False),
        sa.Column('rolename', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('roleid')
    )
    op.create_index(op.f('ix_roles_rolename'), 'roles', ['rolename'], unique=True)

    op.create_table('userroles',
        sa.Column('createdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updatedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deletedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.Column('roleid', sa.Integer(), nullable=False),
        sa.Column('userid', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['roleid'], ['roles.roleid'], ),
        sa.ForeignKeyConstraint(['userid'], ['users.userid'], ),
        sa.PrimaryKeyConstraint('roleid', 'userid')
    )

    op.create_table('items',
        sa.Column('createdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updatedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deletedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.Column('itemid', sa.Integer(), nullable=False),
        sa.Column('itemname', sa.String(length=255), nullable=False),
        sa.Column('itemdescription', sa.Text(), nullable=False),
        sa.Column('itemstock', sa.Integer(), nullable=False),
        sa.Column('itemprice', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('itemid')
    )
    op.create_index(op.f('ix_items_itemname'), 'items', ['itemname'], unique=True)

    op.create_table('baskets',
        sa.Column('createdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updatedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deletedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.Column('basketid', sa.Integer(), nullable=False),
        sa.Column('basketclosed', sa.Boolean(), nullable=False),
        sa.Column('userid', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['userid'], ['users.userid'], ),
        sa.PrimaryKeyConstraint('basketid')
    )

    op.create_table('basketitems',
        sa.Column('createdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updatedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deletedate', sa.DateTime(timezone=True), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.Column('itemid', sa.Integer(), nullable=False),
        sa.Column('basketid', sa.Integer(), nullable=False),
        sa.Column('itemquantity', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['basketid'], ['baskets.basketid'], ),
        sa.ForeignKeyConstraint(['itemid'], ['items.itemid'], ),
        sa.PrimaryKeyConstraint('itemid', 'basketid')
    )

    roles = sa.table('roles', sa.column('roleid', sa.Integer), sa.column('rolename', sa.String))
    op.bulk_insert(roles, [
        {'roleid': 1, 'rolename': 'USER'},
        {'roleid': 2, 'rolename': 'ADMIN'},
    ])


def downgrade():
    op.drop_table('basketitems')
    op.drop_table('baskets')
    op.drop_index(op.f('ix_items_itemname'), table_name='items')
    op.drop_table('items')
    op.drop_table('userroles')
    op.drop_index(op.f('ix_roles_rolename'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_useremail'), table_name='users')
    op.drop_table('users')
