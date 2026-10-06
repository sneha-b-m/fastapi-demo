# Posts API

A small backend built with Python and FastAPI. You can create, view, edit and delete posts. The data is kept in memory, so it disappears when you stop the app.

## Requirements

Python 3.14

## Setup

Create a virtual environment and turn it on:

```bash
python3.14 -m venv .venv
.venv\Scripts\activate        # Mac/Linux: source .venv/bin/activate
```

Install the packages:

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload --port 3000
```

The app runs at http://127.0.0.1:3000/posts

## Try it

Open http://127.0.0.1:3000/docs in your browser. It lists every endpoint, and you can test each one right there.

## Endpoints

| Method | Path | What it does |
|---|---|---|
| POST | `/posts` | Create a post |
| GET | `/posts` | List all posts |
| GET | `/posts/{post_id}` | Get one post |
| PUT | `/posts/{post_id}` | Edit a post |
| DELETE | `/posts/{post_id}` | Delete a post |

A post looks like this:

```json
{
  "id": 1,
  "content": "string",
  "author": "string",
  "created_at": "2026-10-06T07:48:43+00:00"
}
```

## Notes

- Posts are lost when the app restarts.
- A post that doesn't exist returns `404 not found`.