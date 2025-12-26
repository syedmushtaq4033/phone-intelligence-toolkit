# Public footprint search link generator (OSINT-style)

number = "+91900000000"  # dummy example number

search_links = {
    "Google": f"https://www.google.com/search?q={number}",
    "Facebook": f"https://www.facebook.com/search/top/?q={number}",
    "Twitter/X": f"https://twitter.com/search?q={number}"
}

print("Public Footprint Search Links:")
for platform, link in search_links.items():
    print(f"{platform}: {link}")
