---
name: dsh-trends-finder
description: Fetch the latest trending DeepSeek Harness (DSH) plugins, npm downloads, and GitHub stars. Use when a user asks what is popular or top-rated in the DSH ecosystem.
external_urls:
  - https://dsh.so
permissions:
  network: true
  env_vars: false
---

# DSH Trends Finder

## Description
Fetches real-time rankings from the official dsh.so Data API. It returns the top 5 most downloaded plugins this week and the top 5 most starred plugins on GitHub.

## Usage
To run the tool, execute:
    python scripts/run.py

## Output
A formatted text report showing:
1. Top 5 Plugins by weekly npm downloads.
2. Top 5 Plugins by GitHub stars.
