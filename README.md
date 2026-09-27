# ClawMax Hackathon Project
# ClawMax — Momentum Event Follow-Up Agent

Reconnects with people met at Luma events via personalized Gmail follow-ups, using Cognee for memory.

## Setup
1. `python -m venv venv` then activate it
2. `python -m pip install -r requirements.txt`
3. Copy `.env.example` → `.env` and fill in `LLM_API_KEY` and `GMAIL_SENDER`
4. Download `credentials.json` from Google Cloud Console (Gmail API, Desktop App)
5. Export Luma contacts as `contacts.csv` (columns: name, email, fun_fact)
6. Run: `python main.py`