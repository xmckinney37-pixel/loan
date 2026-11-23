# oceaneyez

OpenAI-compatible chat gateway. Clients see the model name **`oceaneyez`**;
the gateway maps it to a real upstream model on Groq.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET  | `/internal/health` | Liveness probe |
| GET  | `/v1/models` | Model discovery (returns `oceaneyez`) |
| POST | `/v1/chat` | Non-streaming completion |
| POST | `/v1/chat/stream` | Server-Sent Events streaming |

All `/v1/*` endpoints require `Authorization: Bearer <APP_API_KEYS>`.

## Deploy (Render, free tier)

1. Push this repo to GitHub
2. Render → **New → Blueprint** → pick this repo → **Apply** (plan: Free)
3. Set `UPSTREAM_API_KEY` = your Groq key (`gsk_...`) in the Environment tab
4. Copy the generated `APP_API_KEYS` value — that's your client key

## Configuration

| Env var | Purpose |
|---|---|
| `UPSTREAM_URL` | Upstream OpenAI-compatible base URL (default: Groq) |
| `UPSTREAM_API_KEY` | Upstream API key (Groq `gsk_...`) |
| `APP_API_KEYS` | Comma-separated client keys (auto-generated on Render) |
| `MODEL_ALIAS` | Name clients see (default: `oceaneyez`) |
| `MODEL_NAME` | Real upstream model (default: `llama-3.3-70b-versatile`) |
