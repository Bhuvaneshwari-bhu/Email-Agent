
---

# Opportunity Agent (Email Intelligence System)

## Overview

Opportunity Agent is an AI-powered system that processes Gmail emails, extracts structured opportunities such as internships, hackathons, scholarships, and fellowships, and stores them in a local database. It also generates daily summaries and provides a CLI interface to query stored data.

---

## Features

* Gmail integration using OAuth authentication
* AI-based email classification and information extraction (Gemini)
* Keyword-based filtering to reduce unnecessary API usage
* Structured storage using SQLite
* Deduplication using unique constraints
* Daily opportunity report generation
* Command-line interface for querying stored opportunities
* Spam and irrelevant email filtering

---

## System Architecture

```
Gmail API
    ↓
sync_gmail.py (email fetcher)
    ↓
keyword filter (pre-processing)
    ↓
agent.py (AI extraction using Gemini)
    ↓
parser.py (JSON parsing)
    ↓
database.py (SQLite storage)
    ↓
daily_report.py (report generation)
    ↓
assistant.py (query interface)
```

---

## Project Structure

```
opportunity-agent/
│
├── gmail_reader.py        Gmail OAuth authentication
├── sync_gmail.py          Gmail email sync and processing
├── agent.py               Gemini-based extraction logic
├── parser.py              JSON parsing utility
├── database.py            SQLite database operations
├── report_generator.py    Report formatting
├── daily_report.py        Daily summary generator
├── assistant.py           CLI-based query system
│
├── credentials.json       OAuth credentials (Google Cloud)
├── token.pickle           Saved authentication token
├── opportunities.db       SQLite database
├── requirements.txt       Project dependencies
└── README.md
```

---

## Workflow

### 1. Gmail Sync

* Connects to Gmail API
* Fetches recent emails
* Extracts subject, sender, and body

### 2. Pre-filtering

* Filters emails using keywords:

  * internship, hackathon, job, scholarship, etc.
* Reduces API calls and cost

### 3. AI Extraction

* Gemini model extracts structured JSON:

```
{
  "category": "Internship",
  "opportunity_name": "Google Summer Internship",
  "deadline": "July 15",
  "action_required": "Submit resume"
}
```

### 4. Storage

* Data stored in SQLite database
* Duplicate prevention using UNIQUE constraint

### 5. Reporting

* Filters important opportunities
* Generates daily summary report

### 6. CLI Assistant

Supports queries such as:

* show all opportunities
* internships
* hackathons

---

## Installation

```bash
git clone https://github.com/Bhuvaneshwari-bhu/Email-Agent.git
cd Email-Agent

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## Setup

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

Place Google OAuth credentials:

```
credentials.json
```

---

## Usage

### Authenticate Gmail

```
python gmail_reader.py
```

### Sync Emails

```
python sync_gmail.py
```

### Generate Daily Report

```
python daily_report.py
```

### Run Assistant

```
python assistant.py
```

---

## Security

* OAuth token stored locally in `token.pickle`
* API keys must be kept in `.env`
* `credentials.json` must not be exposed publicly

---

