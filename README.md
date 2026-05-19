# inkpress-docs

Tiny Flask server that hosts the customer setup guide at `https://docs.inkpress.zorohq.com/readme.txt`.

One big text file (`readme.txt`) covering install, env, Caddy, first login, updates, backups, troubleshooting, security notes, contact.

## Run locally

```
pip install -r requirements.txt
python app.py
# open http://localhost:8505/readme.txt
```

## Deploy

CI builds + pushes via Woodpecker on every push to `main` or `develop`. Container runs on stage at `127.0.0.1:18505`, fronted by Caddy at `docs.inkpress.zorohq.com`.
