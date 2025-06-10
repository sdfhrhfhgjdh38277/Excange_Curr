import requests


class Currency:
    def __init__(self):
        self.api_key = "API-KEY"
        self.supported_currencies = self.get_supported_currencies()

    def get_supported_currencies(self):
        url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/USD"
        response = requests.get(url).json()
        st.error("DEBUG: response from API: ", response)
        if response["result"] == "success":
            return list(response["conversion_rates"].keys())
        else:
            print("Failed to get supported currencies:", response)
            return []

    def convert(self, from_curr, to_curr, amount):
        if (
            from_curr not in self.supported_currencies
            or to_curr not in self.supported_currencies
        ):
            print("One of the currencies is not supported.")
            return None

        url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/pair/{from_curr}/{to_curr}/{amount}"
        response = requests.get(url).json()
        if response["result"] == "success":
            return response["conversion_result"]
        else:
            print("Conversion failed:", response)
            return None


if __name__ == "__main__":
    fromCurr = "USD"
    toCurr = "UAH"
    curr = Currency()
    curr.convert(from_curr=fromCurr, to_curr=toCurr, amount=10)
