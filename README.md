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