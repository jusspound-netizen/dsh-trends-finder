#!/usr/bin/env python3
import urllib.request
import json
import sys

def fetch_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'DSH-Trends-Tool/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def main():
    print("=== DSH PLUGIN TRENDS ===\n")
    
    # 1. Weekly npm Downloads
    data = fetch_json('https://cdn.dsh.so/data/npm-downloads.json')
    if data and 'items' in data:
        print("🔥 Top 5 Fastest Growing (npm Downloads):")
        for item in data['items'][:5]:
            name = item.get('name') or item.get('packageName') or 'Unknown'
            week = item.get('week', 0)
            print(f"  {name} ({week:,} downloads this week)")
    else:
        print("Could not fetch download trends.")

    print("\n")

    # 2. Star Leaderboard
    data = fetch_json('https://cdn.dsh.so/data/stars.json')
    if data and 'boards' in data:
        boards = data['boards']
        plugin_board = boards.get('plugin', {})
        items = plugin_board.get('items', [])
        
        if items:
            print("⭐ Top 5 Most Starred (GitHub):")
            for item in items[:5]:
                name = item.get('name', 'Unknown')
                stars = item.get('stars', 0)
                print(f"  {name} ({stars:,} stars)")
        else:
            print("Could not fetch star trends (no items found).")
    else:
        print("Could not fetch star trends.")

if __name__ == '__main__':
    main()
