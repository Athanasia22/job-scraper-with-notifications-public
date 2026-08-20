import os
from datetime import datetime

# Read sensitive/custom notification topic from Environment / GitHub Secrets
NTFY_TOPIC = os.getenv("NTFY_TOPIC", "demo_academic_alerts")

# Temporal Filtering
CURRENT_YEAR = datetime.now().year
ALLOWED_YEARS = {str(CURRENT_YEAR), str(CURRENT_YEAR - 1)}
EXCLUDE_YEARS = ["2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]  # Exclude older years

# Target Research Portals
PORTALS = [
    {"name": "HCMR Calls", "url": "https://calls.hcmr.gr/category/job-opportunities/"},
    {"name": "CERTH Jobs", "url": "https://www.certh.gr/CCAC170B.el.aspx"},
    {"name": "AUTH Jobs", "url": "https://rc.auth.gr/proskliseis-gia-apasholisi-se-erga"},
    {"name": "FRI Jobs", "url": "https://inale.gr/category/call-for-proposals_el/"},
    {"name": "IKY Scholarships", "url": "https://www.iky.gr/el/ypotrofies-gr"},
    {"name": "ELIDEK Calls", "url": "https://www.elidek.gr/prokirykseis/"},
]

# Keywords to match (Greek & International terms)
KEYWORDS = [
    "βιολογ", "θαλασσ", "βιοπληροφορικ", "πλαγκτ", "ωκεανογραφ",
    "υποτροφ", "metabarcoding", "genomics", "bioinformatics",
    "master", "μεταπτυχιακ", "βιοκοιν", "βιοποικιλ", "βενθικ",
    "παρακολούθηση", "ορμο", "λιμάν",
]

# Administrative terms to exclude
EXCLUDE_KEYWORDS = [
    "πρακτικο", "αποτελεσματα", "οριστικα", "προσωρινα", "αποφαση",
]

SEEN_JOBS_FILE = "seen_jobs.txt"
REQUEST_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}