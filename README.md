# ai-attendance-voice-face-reco

## Local setup

Create `.streamlit/secrets.toml` in the project directory:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-supabase-anon-key"
```

Then start the Streamlit app from the project directory:

```powershell
streamlit run app.py
```

The same values can also be provided through the `SUPABASE_URL` and
`SUPABASE_KEY` environment variables.