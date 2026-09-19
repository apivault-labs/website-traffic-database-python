from website_traffic_database import WebsiteTrafficDatabaseClient

for count in (10, 100, 1000):
    print(count, WebsiteTrafficDatabaseClient.estimate_cost(count), "USD estimated result charges")
