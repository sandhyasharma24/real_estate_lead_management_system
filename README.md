# AI-Powered Real Estate Lead Scoring

A small FastAPI service that retrieves a real-estate lead from a local SQLite database and uses a locally running Ollama model to classify the lead as **Hot**, **Warm**, or **Cold** based on the lead's name and budget.

> This README describes the implementation currently present in the repository.

## Current implementation

The backend exposes a single scoring endpoint:

```text
GET /score_lead/{email}
```

The flow is:

1. Look up the lead by email in `leads.db`.
2. Read the lead's name, email, and budget.
3. Send the lead information to an Ollama chat model.
4. Ask the model to classify the lead as `Hot`, `Warm`, or `Cold`.
5. Return the model's result as JSON.

## Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **SQLite**
- **Ollama**
- **Mistral model**

## API

### Score a lead

```http
GET /score_lead/{email}
```

Example response:

```json
{
  "lead_score": "Hot"
}
```

If the email is not present in the database:

```json
{
  "message": "Lead not found"
}
```

## Local setup

### Prerequisites

- Python 3.x
- Ollama installed locally
- The Mistral model available in Ollama

### Install dependencies

Install the Python packages used by the application:

```bash
pip install fastapi uvicorn pydantic ollama
```

### Start the API

From the repository root:

```bash
uvicorn backend:app --reload
```

The API will be available at the local address shown by Uvicorn.

## Database

The application expects a SQLite database named:

```text
leads.db
```

The current backend expects a `leads` table containing the lead data used by the scoring endpoint.

## Repository files

- `backend.py` — FastAPI application and AI scoring logic
- `querry.py` — simple SQLite query utility for inspecting stored leads
- `test.py` — experimental OpenAI API test
- `leads.db` — current SQLite database

## Notes

The project currently focuses on the core AI lead-scoring flow. Features such as a full lead-management dashboard, automated outreach, multi-source ingestion, and production authentication are **not currently implemented in the repository**.

## Author

**Sandhya Sharma**

[GitHub](https://github.com/sandhyasharma24)
