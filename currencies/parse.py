import requests


class Currency:
    def __init__(self):
        pass

    def convert(self, from_curr, to_curr, amount):
        url = f"https://v6.exchangerate-api.com/v6/183746f5f8587ca8e2703602/pair/{from_curr}/{to_curr}/{amount}"
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
