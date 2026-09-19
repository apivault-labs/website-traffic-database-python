# Website Traffic Database — Python SDK

Python client for the [Website Traffic Database Apify Actor](https://apify.com/apivault_labs/website-traffic-database). Send public Actor inputs, wait for the hosted run, and receive clean Dataset rows without maintaining scraping infrastructure.

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue)](https://apify.com/apivault_labs/website-traffic-database)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Results

- Traffic and rank filters
- Country and category discovery
- Growth and engagement signals
- Direct domain and similar-site workflows

Traffic values are estimates. The wrapper exposes only the Actor's public contract; processing remains inside the hosted Actor.

## Install

```bash
pip install git+https://github.com/apivault-labs/website-traffic-database-python.git
```

Create an Apify token at [Console → Integrations](https://console.apify.com/account/integrations), then:

```python
from website_traffic_database import WebsiteTrafficDatabaseClient

client = WebsiteTrafficDatabaseClient(api_token="apify_api_xxxxxx")
rows = client.run({'workflow': 'auto',
 'country': 'US',
 'minVisits': 10000,
 'onlyGrowing': True,
 'maxResults': 100})
print(rows[0] if rows else "No results")
```

You can set `APIFY_API_TOKEN` instead of passing the token in code.

## Public input options

| Field | Type | Default | Description |
|---|---|---|---|
| `workflow` | `string` | `auto` | Discover websites, inspect domains or find similar sites. |
| `minVisits` | `integer` | `0` | Minimum estimated monthly visits. |
| `maxVisits` | `integer` | `0` | Optional maximum estimated monthly visits. |
| `category` | `string` | `` | Website category filter. |
| `country` | `string` | `` | ISO-2 country code. |
| `hasAiTraffic` | `boolean` | `False` | Keep sites with detected AI referral traffic. |
| `onlyGrowing` | `boolean` | `False` | Keep sites with positive traffic growth. |
| `minGrowthPercent` | `number` | `0` | Minimum growth percentage. |
| `keyword` | `string` | `` | Match a domain or site name. |
| `trafficSource` | `string` | `` | Traffic source to filter by. |
| `maxBounce` | `number` | `0` | Optional maximum bounce rate. |
| `minPagesPerVisit` | `number` | `0` | Minimum pages per visit. |
| `maxResults` | `integer` | `100` | Maximum number of returned rows. |
| `sortBy` | `string` | `visits` | Public field used to order results. |
| `sortOrder` | `string` | `desc` | Ascending or descending order. |
| `outputPreset` | `string` | `outreach` | Choose a public result layout. |
| `domains` | `array` | `[]` | Domains to inspect directly. |
| `similarTo` | `string` | `` | Domain used to discover similar websites. |

The complete, versioned schema is also available on the [Actor page](https://apify.com/apivault_labs/website-traffic-database).

## Pricing

Pay per delivered result through Apify, starting around **$7/1,000 results** on paid tiers. Free-plan pricing and platform usage can differ; check the Actor page before large runs.

## Examples

- `examples/quickstart.py` — first run
- `examples/bulk_analysis.py` — expand a target list
- `examples/export_csv.py` — save flat result fields
- `examples/save_json.py` — preserve nested output
- `examples/cost_estimate.py` — estimate result-event charges
- `examples/environment_token.py` — keep credentials out of code

## Architecture and privacy

This repository is intentionally a thin API client. Collection, retries, analysis and billing run inside the hosted Apify Actor. No private implementation, credentials, scoring weights or infrastructure configuration are included.

## License

MIT. The hosted Actor is a separate paid service governed by Apify terms.
