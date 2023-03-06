import os
from pathlib import Path

from project import ROOT
from dotenv import load_dotenv

load_dotenv(ROOT / ".env")

BLEND_OUT_DIR = Path(os.environ.get("BLEND_OUT_DIR"))
