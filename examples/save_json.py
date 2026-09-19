import json
from website_traffic_database import WebsiteTrafficDatabaseClient

rows = WebsiteTrafficDatabaseClient().run({'workflow': 'auto',
 'country': 'US',
 'minVisits': 10000,
 'onlyGrowing': True,
 'maxResults': 100})
with open("results.json", "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=2)
