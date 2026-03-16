# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **educational tutorial repository** teaching AI-assisted development workflows. The content guides participants through building an e-commerce sales dashboard using Python and Streamlit, while learning spec-driven development, Git/GitHub, Jira project management, and Claude Code.

There is no build system, test suite, or deployable application in this repo — only tutorial documentation and sample data.

## Repository Structure

- `v2/` — Current tutorial format (async pre-work + 3-hour live workshop)
  - `pre-work-setup.md` — 60-90 min self-paced setup guide
  - `workshop-build-deploy.md` — 3-hour live workshop guide
- `v1/` — Original multi-session tutorial format (legacy)
- `prd/ecommerce-analytics.md` — Product Requirements Document students build from
- `data/sales-data.csv` — Sample dataset (~482 transactions, Jan–Dec 2024)

## What Students Build

A Streamlit dashboard backed by `data/sales-data.csv` with:
- KPI cards (Total Sales, Total Orders)
- Sales trend line chart
- Category and region breakdown bar charts

**Tech stack:** Python 3.11+, Streamlit, Plotly, Pandas. Deployed to Streamlit Community Cloud.

## Tutorial Workflow

The workflow taught in the tutorials:

```
PRD → spec-kit (structured plan) → Jira issues → Build with Claude Code → Git commit/push → Deploy
```

Key commands students run during the workshop:
```bash
spec-kit init                           # Generate structured plan from PRD
streamlit run app.py                    # Run dashboard locally
git checkout -b feature/dashboard       # Create feature branch
git commit -m "ECOM-1: add KPI cards"  # Commit with Jira traceability
git push -u origin feature/dashboard   # Push and open PR
```

## Content Conventions

- **v2 is the canonical tutorial.** V1 is legacy; do not update v1 unless explicitly asked.
- Jira issue IDs use the `ECOM-` prefix (e.g., `ECOM-1`, `ECOM-2`).
- Git commit messages in examples follow the format: `ECOM-{N}: {imperative description}`.
- All code blocks must be labeled with where to run them (terminal, Claude Code, browser, etc.) — this is an established pattern in the existing docs.
- The workshop is delivered live over Zoom; timing annotations (e.g., `[10 min]`) in `workshop-build-deploy.md` are intentional.
