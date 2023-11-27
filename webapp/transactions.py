import json
import requests
import pandas as pd

from main import Config


class Transactions:
    USDT = "THPvaUhoh2Qn2y9THCZML3H815hhFhn5YC"

    def get_objects(self, address: str = USDT, limit: int = 20) -> json:
        url = f"https://api.shasta.trongrid.io/v1/accounts/{address}/transactions/trc20"
        headers = {"accept": "application/json"}
        params = {'limit': limit}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def calculate_risk_score(self, weights: list, anomalies: list) -> float:
        total_weight = sum(weights)
        risk_score = sum(w * a for w, a in zip(weights, anomalies)) / total_weight
        return risk_score

    def assess_risk(self) -> float:
        json_response = self.get_objects()
        weights = []
        anomaly_scores = []

        for entry in json_response.get('data', []):
            weight = entry.get('token_info', {}).get('decimals', 0)
            anomaly_score = int(entry.get('value', 0))
            weights.append(weight)
            anomaly_scores.append(anomaly_score)

        risk_score = self.calculate_risk_score(weights, anomaly_scores)
        return risk_score

    def chain_analysis(self):
        transactions = self.get_objects().get('data', [])
        results = []

        for transaction in transactions:
            type = transaction["type"]
            amount = transaction["value"]

            if type == "Transfer" and int(amount) > 1000000:
                result = {
                    'transaction_id': transaction['transaction_id'],
                    'from': transaction["from"],
                    'to': transaction["to"],
                    'value': amount
                }
                results.append(result)

        return results

    def detect_address_changes(self, transactions):
        address_changes = transactions['to'].ne(transactions['to'].shift())

        if address_changes.any():
            return 'There are frequent changes of addresses in the chain of transactions.'
        else:
            return 'No frequent changes in addresses were detected in the transaction chain.'

    def detect_mixers(self, transactions):
        mixer_address = Config.MIXER

        if mixer_address in transactions['to'].values:
            return f'Detected use of "mixer" (address: {mixer_address}).'
        else:
            return 'The use of "mixers" was not detected.'

    def start_checking(self):
        data = self.get_objects()
        massage = {}

        transactions = pd.DataFrame(data['data'])

        massage['detect_address'] = self.detect_address_changes(transactions)
        massage['detect_mixers'] = self.detect_mixers(transactions)
        massage['suspicious_transactions'] = self.chain_analysis()
        return massage


if __name__ == '__main__':
    a = Transactions()
    # print(a.chain_analysis())
    print(a.start_checking())
    # print(a.get_objects())
