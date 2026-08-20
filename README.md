# 🧬 Automated Academic & Research Opportunity Scraper

A lightweight Python automation engine that monitors Hellenic research institutes and university portals for biological, marine science, and bioinformatics opportunities, delivering real-time mobile alerts via the ntfy protocol.

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

## 🚀 Quick Start for Forked Repositories

1. **Fork** this repository.
2. **Customize your search:** Adjust your target portals, keywords, and exclusions in `config.py`.
3. **Configure Secrets & Permissions:** Follow the setup steps below so GitHub Actions can run safely.
4. **Subscribe to alerts:** Connect your phone or browser to your custom ntfy topic.

---

## 🔐 GitHub Secrets & Permissions Setup

### 1. Add your private `NTFY_TOPIC`
1. Go to your repository's **Settings** tab.
2. In the left sidebar, navigate to **Security** $\rightarrow$ **Secrets and variables** $\rightarrow$ **Actions**.
3. Click the green **New repository secret** button in the top right.
4. Set the fields:
   * **Name:** `NTFY_TOPIC`
   * **Secret:** Your chosen private topic name *(e.g., `my_custom_academic_alerts`)*
5. Click **Add secret**.

### 2. Enable Workflow Write Permissions (Required)
1. In the repository **Settings**, go to the left sidebar and select **Actions** $\rightarrow$ **General**.
2. Scroll to the bottom to the **Workflow permissions** section.
3. Select **Read and write permissions** *(this allows the bot to update `seen_jobs.txt` automatically)*.
4. Click **Save**.

---

## 📲 Setting Up ntfy Alerts

ntfy is completely free and requires no account or registration.

* **Mobile App (iOS / Android):**
  1. Download the **ntfy** app.
  2. Tap **`+`**, type your chosen topic secret name, and tap **Subscribe**.
* **Web Browser:**
  * Open `https://ntfy.sh/<your_topic_name>` in your browser to view alerts directly.