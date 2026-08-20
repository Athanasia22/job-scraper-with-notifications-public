 # 🧬 Automated Academic & Research Opportunity Scraper

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.11
* **Web Scraping:** `BeautifulSoup4`, `Requests`, `urllib.parse`
* **Automation & CI/CD:** GitHub Actions (Scheduled Cron Workflows)
* **Mobile Alerts:** ntfy.sh REST API with UTF-8 byte-stream encoding
* **State Management:** Git-backed append-only archive (`seen_jobs.txt`)

---

## 🎯 Portals Monitored

* **HCMR** (Hellenic Centre for Marine Research)
* **CERTH** (Centre for Research & Technology Hellas)
* **AUTH** (Aristotle University of Thessaloniki - Research Committee)
* **FRI / INALE** (Fisheries Research Institute)
* **IKY** (State Scholarships Foundation)
* **ELIDEK** (Hellenic Foundation for Research & Innovation)

---

## ⚙️ Core Features

* **Multi-Keyword Filtering:** Scans for marine biology, metabarcoding, genomics, bioinformatics, and fellowship opportunities.
* **Administrative Noise Reduction:** Automatically drops committee minutes, intermediate decisions, and formal approval listings.
* **Stateful Deduplication:** Persists processed URLs across serverless execution environments to prevent duplicate push alerts.
* **Serverless Execution:** Runs at zero cost entirely on GitHub Actions runners without requiring private server infrastructure.

---

## 🚀 Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/<repo-name>.git
   cd <repo-name>

   A lightweight Python automation engine that monitors Hellenic research institutes and university portals for biological, marine science, and bioinformatics opportunities, delivering real-time mobile alerts via the ntfy protocol.

Click the Settings tab at the top of the page .In the left-hand sidebar, scroll down to the Security section and click on Secrets and variables Actions. </p>
<p>Click the green New repository secret button in the top right.</p>
<p>In the Name field, type exactly NTFY_TOPIC</p>
In the Secret field, paste your private topic name.Click the green Add secret button.Verify Workflow Permission (One-time check).
<p>While you are in Settings:Go to the left sidebar Actions General.Scroll to the bottom to Workflow permissions.Select Read and write permissions.Click Save. </p>


<h1>NTFY</h1>
 Pick a New Topic secret name from web or app. Subscribe
 OR 
 in your browser enter the name after the first part of the link: [https://ntfy.sh/random_name]
