from website_traffic_database import WebsiteTrafficDatabaseClient

client = WebsiteTrafficDatabaseClient()
rows = client.run({'workflow': 'auto',
 'country': 'US',
 'minVisits': 10000,
 'onlyGrowing': True,
 'maxResults': 100})
print(rows[0] if rows else "No results")
