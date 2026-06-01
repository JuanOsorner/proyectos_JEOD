import requests

class BitcoinService:

    URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

    @staticmethod
    def get_bitcoin_prices(days: int = 30) -> dict:
        """
        Obtiene precios históricos de Bitcoin y los transforma
        a un formato adecuado para regresión lineal.

        Retorna:

        {
            "x": [0, 1, 2, ...],
            "y": [precio_0, precio_1, precio_2, ...]
        }
        """

        params = {
            "vs_currency": "usd",
            "days": days,
            "interval": "daily"
        }

        response = requests.get(
            BitcoinService.URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        prices = data.get("prices", [])

        x = []
        y = []

        # Por el momento dejamos index de esta manera para manejar los ultimos 30 dias
        for index, price_data in enumerate(prices):
            # El timestamp lo podemos usar para trabajar con todos los datos desde 1970
            # Por el momento lo igniramos
            timestamp = price_data[0]  # No lo usamos por ahora
            price = price_data[1]

            x.append(index)
            y.append(price)

        return {
            "x": x,
            "y": y
        }