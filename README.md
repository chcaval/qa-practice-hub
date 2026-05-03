# QA Practice Hub

A full-stack application built specifically to practice the **testing pyramid** — from unit tests up to end-to-end tests, with CI/CD automation.

**Stack:** FastAPI · SQLite · React/Vite · Playwright · pytest · GitHub Actions

---

## What's in here

```
backend/          FastAPI REST API (users + AI summarize endpoint)
frontend/         React UI for creating users
e2e/              Playwright end-to-end tests
.github/          GitHub Actions CI pipeline
docker-compose.yml  Runs app + Postgres together
```

---

## Running the app

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API runs at `http://localhost:8000`. Docs at `http://localhost:8000/docs`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

UI runs at `http://localhost:3000`.

---

## Running the tests

### Unit + Integration tests (pytest)

```bash
cd backend
source venv/bin/activate
python -m pytest -v
```

58 tests across three layers:

| Layer | File | What it tests |
|---|---|---|
| Unit | `tests/unit/test_schemas.py` | Pydantic schema validation |
| Unit | `tests/unit/test_ai_service.py` | AIService logic with mocks |
| Integration | `tests/integration/test_users_api.py` | Full HTTP + real DB |
| AI | `tests/ai/test_summarize_endpoint.py` | Summarize endpoint contract |

### End-to-end tests (Playwright)

Requires the backend and frontend both running first.

```bash
cd e2e
npx playwright test
```

Tests:
- Creates a user successfully (happy path)
- Shows error when email is already registered

---

## Key testing concepts demonstrated

**Mocking** — `test_ai_service.py` injects a `MagicMock` in place of a real LLM client, so tests run fast and deterministically without hitting any external API.

**Fixtures** — `conftest.py` sets up an in-memory SQLite database and a fresh FastAPI test client for every integration test, guaranteeing test isolation.

**Parametrize** — `test_ai_service.py` uses `@pytest.mark.parametrize` to run the same assertion across multiple inputs without duplicating test code.

**Error path testing** — both unit and integration tests cover failure cases: empty input, duplicate email, 404s, and client-side failures that should surface as `RuntimeError`.

**Coverage** — `ai_service.py` has 100% test coverage. Overall backend coverage is 95%.

---

## CI/CD

Every push to `main` triggers GitHub Actions (`.github/workflows/ci.yml`), which:
1. Installs dependencies
2. Runs the full pytest suite
3. Reports pass/fail on the commit

---

## API endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/users` | List all users |
| POST | `/users` | Create a user |
| GET | `/users/{id}` | Get a user by ID |
| PUT | `/users/{id}` | Update a user |
| DELETE | `/users/{id}` | Delete a user |
| POST | `/ai/summarize` | Summarize text (mocked LLM) |
