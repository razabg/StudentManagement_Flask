use this structure:
```
run the docker compose
docker exec -it pyserver flask --app manage.py  db init
docker exec -it pyserver flask --app manage.py db migrate -m "build tables"
docker exec -it pyserver flask --app manage.py db upgrade

├── app
│   ├── __init__.py
│   ├── main
│   │   ├── controller
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   └── test
│       └── __init__.py
└── requirements.txtcommit - with docker