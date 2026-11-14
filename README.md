# DSH Trends Finder

[![Agensi](https://img.shields.io/badge/Agensi-AI_Agent_Skills-blue)](https://www.agensi.io/r/CONTEXTBRIDGE?to=/creators/context-bridge)

A lightweight, zero-dependency Python CLI that fetches live market data from the DeepSeek Harness (DSH) ecosystem.

Instead of manually checking the registry, this tool queries the official `dsh.so` Data API and outputs a clean report of what is trending right now.

## What it does

- **Top 5 npm Downloads:** Shows the fastest-growing plugins by weekly downloads.
- **Top 5 GitHub Stars:** Shows the most popular plugins by star count.

## Usage

Requires Python 3.9+. No external packages needed.

```bash
python scripts/run.py
```

**Example Output:**
```text
=== DSH PLUGIN TRENDS ===

🔥 Top 5 Fastest Growing (npm Downloads):
  @ranxianglei/billion-context (954,773 downloads this week)
  @helloHub1212/dsh-windows-mcp (705,401 downloads this week)
  dsh-market (555,424 downloads this week)

⭐ Top 5 Most Starred (GitHub):
  @Ebony-Vinyl/dsh-our-free-model (69,556 stars)
  learn-harness-engineering (24,380 stars)
```

## How it works

This tool is a thin wrapper around the public [dsh.so Data API](https://www.dsh.so/data-api). It uses only the Python standard library (`urllib` and `json`) to fetch and parse the JSON feeds. It makes no network calls beyond `cdn.dsh.so`.

## License

MIT

---

### Ready-to-use Agent Skills
Want your AI agent to use these tools automatically? Browse my full catalog of AI agent skills for Jira, Sentry, DevOps, and agent observability on Agensi.
> **[View my Agensi storefront](https://www.agensi.io/r/CONTEXTBRIDGE?to=/creators/context-bridge)**
