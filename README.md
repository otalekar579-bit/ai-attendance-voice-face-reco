# ai-attendance-voice-face-reco

## Local setup

Use Python 3.11 for the project. The voice pipeline depends on the compiled
`webrtcvad` package, which is already available in the included virtual
environment.

Activate the environment before installing or running the app:

```powershell
cd "C:\Users\otale\OneDrive\Desktop\python project\ai-attendance"
.\venv\Scripts\Activate.ps1
```

Create `.streamlit/secrets.toml` in the project directory:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-supabase-anon-key"
```

Use the exact Project URL shown in Supabase under **Project Settings > API**.
The URL must resolve to a real `*.supabase.co` hostname; a deleted project or
mistyped URL causes login connection errors.

Then start the Streamlit app from the project directory:

```powershell
streamlit run app.py
```

The same values can also be provided through the `SUPABASE_URL` and
`SUPABASE_KEY` environment variables.