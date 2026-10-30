# Task API

A small Flask API for practicing how to package and run a Python web service.
Tasks are kept in memory, so they reset whenever the process restarts.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

The server listens on port `8000` by default. Set the `PORT` environment
variable to use another port.

Open [http://localhost:8000](http://localhost:8000) for the API guide and
example requests.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Show the API guide |
| `GET` | `/health` | Check that the service is running |
| `GET` | `/tasks` | List tasks |
| `POST` | `/tasks` | Create a task |
| `DELETE` | `/tasks/<id>` | Delete a task |

Create a task by sending a JSON object with a non-empty `title`, for example:

```json
{"title": "Learn Docker"}
```

## Run tests

```powershell
python -m unittest
```
