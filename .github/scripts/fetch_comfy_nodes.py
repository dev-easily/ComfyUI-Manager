import requests
import os
import json

base_url = "https://api.comfy.org/nodes"
form_factors = [
    "desktop-win", "desktop-mac", "git-windows", "git-mac", "git-linux", "other"
]

os.makedirs(".ci/comfy", exist_ok=True)

for form_factor in form_factors:
    page = 1
    all_nodes = []
    while True:
        url = f"{base_url}?page={page}&limit=30&form_factor={form_factor}"
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        all_nodes.extend(data["nodes"])
        if page >= data["totalPages"]:
            break
        page += 1
    with open(f".ci/comfy/nodes-{form_factor}.json", "w", encoding="utf-8") as f:
        json.dump({"nodes": all_nodes}, f, ensure_ascii=False, indent=2) 