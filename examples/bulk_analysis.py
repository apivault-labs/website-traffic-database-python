from website_traffic_database import WebsiteTrafficDatabaseClient

client = WebsiteTrafficDatabaseClient()
payload = {'workflow': 'auto',
 'country': 'US',
 'minVisits': 10000,
 'onlyGrowing': True,
 'maxResults': 100}
# Add more targets or queries to the list fields supported by this Actor.
rows = client.run(payload)
print(f"Received {len(rows)} rows")
