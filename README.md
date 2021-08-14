# bug-tracker
Simple bug-tracker system

## Install dependencies
```bash
$ pip install -r requirements.txt
```

## Activate your environment
```bash
$ python -m venv venv && source venv/bin/activate
```

## Run your app

```bash
$ export FLASK_APP=app.py FLASK_ENV=development && flask run
```

**Note**: If you're using Windows try "set":
```bash
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
$ python -m flask run
```