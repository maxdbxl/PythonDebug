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

## Indices

Performance
- Lister les utilisateurs devient très lent
- Afficher tous les paniers génère beaucoup de requêtes
- Le rapport des commandes interroge la base en boucle
- La liste des utilisateurs reste lente sans SQL supplémentaire
- La recherche à faible stock charge toute la table
- Les statistiques chargent tout pour compter
- L'attribution des rôles répète du travail

Sécurité
- Le mot de passe est exposé
- Le token contient trop d'informations
- Un utilisateur peut consulter le profil d'un autre
- La recherche d'articles n'est pas sûre
- Debug et clé secrète en production
- CORS trop permissif
- Le token peut passer par l'URL

Logique métier
- Des rôles se mélangent entre utilisateurs
- Une comparaison de liste trompeuse
- Ajouter deux fois le même article
- Le stock après une commande
- Total du panier faux au centime
- Les articles supprimés apparaissent encore

Robustesse
- Un id inexistant plante
- Les erreurs sont ignorées
- La suppression efface l'historique
- L'injecteur garde des données en mémoire
