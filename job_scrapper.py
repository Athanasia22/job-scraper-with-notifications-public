import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from config import (
    NTFY_TOPIC, ALLOWED_YEARS, EXCLUDE_YEARS, PORTALS,
    KEYWORDS, EXCLUDE_KEYWORDS, SEEN_JOBS_FILE, REQUEST_HEADERS
)

def load_seen_links():
    if not os.path.exists(SEEN_JOBS_FILE):
        return set()
    with open(SEEN_JOBS_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

def save_seen_links(seen_links):
    with open(SEEN_JOBS_FILE, "w", encoding="utf-8") as f:
        for link in seen_links:
            f.write(f"{link}\n")

def is_recent_post(article_url, snippet_text):
    combined_text = f"{snippet_text} {article_url}".lower()
    if any(year in combined_text for year in ALLOWED_YEARS):
        return True
    if any(old_yr in combined_text for old_yr in EXCLUDE_YEARS):
        return False
    return True

def send_ntfy_alert(match):
    endpoint = f"https://ntfy.sh/{NTFY_TOPIC}"
    message = f"Institution: {match['portal']}\nTitle: {match['title']}"
    headers = {
        "Title": "New Research Call Alert",
        "Priority": "high",
        "Tags": "briefcase,microscope",
        "Click": match["url"],
    }
    try:
        response = requests.post(
            endpoint, data=message.encode("utf-8"), headers=headers, timeout=10
        )
        if response.status_code == 200:
            print(f"[✓] Alert sent: {match['title']}")
        else:
            print(f"[✗] ntfy error: {response.status_code}")
    except Exception as e:
        print(f"[✗] Request failed: {e}")

def check_portals():
    seen_links = load_seen_links()
    new_matches = []

    for portal in PORTALS:
        portal_name = portal["name"]
        portal_url = portal["url"]
        print(f"Checking {portal_name}...")

        try:
            response = requests.get(portal_url, headers=REQUEST_HEADERS, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            for link in soup.find_all("a"):
                text = link.get_text(strip=True)
                href = link.get("href")

                if not href or not text or len(text) < 5:
                    continue

                full_url = urljoin(portal_url, href)
                content_to_check = f"{text} {full_url}".lower()

                has_keyword = any(kw.lower() in content_to_check for kw in KEYWORDS)
                is_excluded = any(ex.lower() in content_to_check for ex in EXCLUDE_KEYWORDS)

                if has_keyword and not is_excluded:
                    if full_url not in seen_links:
                        if is_recent_post(full_url, text):
                            match = {"portal": portal_name, "title": text, "url": full_url}
                            send_ntfy_alert(match)
                            seen_links.add(full_url)
                            new_matches.append(match)
                        else:
                            print(f"[SKIP] Outdated listing: {text}")
                            seen_links.add(full_url)

        except Exception as e:
            print(f"[✗] Error processing {portal_name}: {e}")

    save_seen_links(seen_links)
    print(f"[OK] Run complete. {len(new_matches)} new calls processed.")

if __name__ == "__main__":
    check_portals()