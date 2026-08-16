import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://chbmcijdkxqyblxqrull.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "sb_publishable_UA3C1NOnHm6dehrPT6cu6w_wwqMMsSI")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
