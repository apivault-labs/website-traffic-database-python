import os
from website_traffic_database import WebsiteTrafficDatabaseClient

if not os.environ.get("APIFY_API_TOKEN"):
    raise SystemExit("Set APIFY_API_TOKEN before running this example")
client = WebsiteTrafficDatabaseClient()
print(client.run_one({'workflow': 'auto',
 'country': 'US',
 'minVisits': 10000,
 'onlyGrowing': True,
 'maxResults': 100}))
