import requests
from typing import List, Dict

COINPAPRIKA_URL = "https://api.coinpaprika.com/v1/tickers"
COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"

def fetch_coinpaprika(limit: int = 10) -> List[Dict]:
    """
    Fetch top cryptocurrencies from CoinPaprika (no API key required)
    """
    response = requests.get(COINPAPRIKA_URL)
    response.raise_for_status()
    data = response.json()
    # Return only top 'limit' coins
    return data[:limit]

def fetch_coingecko(vs_currency: str = "usd", limit: int = 10) -> List[Dict]:
    """
    Fetch top cryptocurrencies from CoinGecko (free, no key required)
    """
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(COINGECKO_URL, params=params)
    response.raise_for_status()
    return response.json()

def ingest_crypto_data() -> List[Dict]:
    """
    Fetch data from both CoinPaprika and CoinGecko,
    and convert it into the standard ETL format.
    """
    paprika_data = fetch_coinpaprika(limit=10)
    gecko_data = fetch_coingecko(limit=10)

    combined = []
    for coin in paprika_data:
        combined.append({
            "source_id": coin.get("id", "unknown"),
            "data": str(coin)
        })
    for coin in gecko_data:
        combined.append({
            "source_id": coin.get("id", "unknown"),
            "data": str(coin)
        })
    return combined
