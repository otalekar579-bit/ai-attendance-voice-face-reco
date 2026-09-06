import os

import streamlit as st
from supabase import Client, create_client


def _get_setting(name):
    try:
        return st.secrets[name]
    except (FileNotFoundError, KeyError):
        return os.getenv(name)


supabase_url = _get_setting("SUPABASE_URL")
supabase_key = _get_setting("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise RuntimeError(
        "Missing Supabase credentials. Add SUPABASE_URL and SUPABASE_KEY "
        "to .streamlit/secrets.toml or set them as environment variables."
    )

supabase: Client = create_client(supabase_url, supabase_key)