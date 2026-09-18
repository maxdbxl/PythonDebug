# Start project

```shell
docker compose up -d
```

```shell
python -m venv .venv
```
Sous linux
```shell
source .venv/bin/activate
```

sous windows
```shell
.venv/bin/Activate.ps1
```

```shell
pip install -r requirements.txt
```

```shell
flask db init
flask db upgrade
```

```shell
python seed.py
```

Lancer le server via le debugger vscode/pycharm/...
## Routes

| Méthode | Route | Query params | Droits | Form |
|---|---|---|---|---|
| GET | `/` | | | |
| POST | `/api/login` | | | [UserLoginForm](app/forms/user/user_login_form.py) |
| GET | `/api/users` | | USER | |
| GET | `/api/users/<userid>` | | USER | |
| POST | `/api/users/register` | | | [UserRegisterForm](app/forms/user/user_register_form.py) |
| PUT | `/api/users/<userid>` | | ADMIN ou soi-même | [UserUpdateForm](app/forms/user/user_update_form.py) |
| GET | `/api/items` | | | |
| GET | `/api/items/<itemid>` | | | |
| GET | `/api/items/search` | `q` | | |
| GET | `/api/items/low-stock` | `threshold` | | |
| POST | `/api/items/add` | | ADMIN | [ItemForm](app/forms/item/item_form.py) |
| PUT | `/api/items/<itemid>` | | ADMIN | [ItemForm](app/forms/item/item_form.py) |
| GET | `/api/basket` | | USER | |
| PUT | `/api/basket/` | | USER | [BasketAddItemForm](app/forms/basket/basket_add_item_form.py) |
| DELETE | `/api/basket/<itemid>` | | USER | |
| POST | `/api/basket/checkout` | | USER | |
| GET | `/api/basket/all` | | ADMIN | |
| GET | `/api/basket/report` | | ADMIN | |
| GET | `/api/stats` | | | |
