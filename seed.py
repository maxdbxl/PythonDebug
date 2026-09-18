import random

import bcrypt

from app import app, db
from app.models.basket import Basket
from app.models.basket_item import BasketItem
from app.models.item import Item
from app.models.role import Role
from app.models.user import User
from app.models.user_role import UserRole

NB_USERS = 300
NB_ITEMS = 200

ADJECTIVES = ['Blue', 'Fast', 'Silent', 'Golden', 'Cosmic', 'Vintage', 'Electric',
              'Wooden', 'Ceramic', 'Digital', 'Organic', 'Premium', 'Compact', 'Rugged']
NOUNS = ['Widget', 'Gadget', 'Lamp', 'Chair', 'Bottle', 'Backpack', 'Keyboard',
         'Speaker', 'Mug', 'Notebook', 'Camera', 'Charger', 'Wallet', 'Umbrella']


def clear():
    db.session.query(BasketItem).delete()
    db.session.query(Basket).delete()
    db.session.query(UserRole).delete()
    db.session.query(User).delete()
    db.session.query(Item).delete()
    db.session.commit()


def ensure_roles():
    if Role.query.filter_by(rolename="USER").first() is None:
        db.session.add(Role(roleid=1, rolename="USER"))
    if Role.query.filter_by(rolename="ADMIN").first() is None:
        db.session.add(Role(roleid=2, rolename="ADMIN"))
    db.session.commit()


def seed():
    with app.app_context():
        clear()
        ensure_roles()

        password_hash = bcrypt.hashpw(b'password', bcrypt.gensalt()).decode('utf-8')
        role_user = Role.query.filter_by(rolename="USER").one()
        role_admin = Role.query.filter_by(rolename="ADMIN").one()

        admin = User(username="admin", useremail="admin@shop.local",
                     userpassword=password_hash, userdescription="platform administrator")
        db.session.add(admin)
        db.session.flush()
        db.session.add(UserRole(userid=admin.userid, roleid=role_user.roleid))
        db.session.add(UserRole(userid=admin.userid, roleid=role_admin.roleid))

        users = [admin]
        for i in range(1, NB_USERS + 1):
            u = User(username=f"user{i}", useremail=f"user{i}@shop.local",
                     userpassword=password_hash,
                     userdescription=f"Customer number {i} living at 42 Main Street.")
            db.session.add(u)
            db.session.flush()
            db.session.add(UserRole(userid=u.userid, roleid=role_user.roleid))
            users.append(u)
        db.session.commit()

        items = []
        used = set()
        for i in range(NB_ITEMS):
            while True:
                name = f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)} {i}"
                if name not in used:
                    used.add(name)
                    break
            it = Item(itemname=name,
                      itemdescription=f"A very nice {name.lower()} for everyday use.",
                      itemstock=random.randint(0, 50),
                      itemprice=round(random.uniform(1.99, 199.99), 2))
            db.session.add(it)
            items.append(it)
        db.session.commit()

        for u in users:
            closed = Basket(userid=u.userid, basketclosed=True)
            db.session.add(closed)
            db.session.flush()
            for it in random.sample(items, random.randint(3, 10)):
                db.session.add(BasketItem(basketid=closed.basketid, itemid=it.itemid,
                                          itemquantity=random.randint(1, 4)))

            open_basket = Basket(userid=u.userid, basketclosed=False)
            db.session.add(open_basket)
            db.session.flush()
            for it in random.sample(items, random.randint(1, 5)):
                db.session.add(BasketItem(basketid=open_basket.basketid, itemid=it.itemid,
                                          itemquantity=random.randint(1, 4)))
        db.session.commit()

        print(f"seeded {len(users)} users, {len(items)} items, {len(users) * 2} baskets")


if __name__ == '__main__':
    seed()
