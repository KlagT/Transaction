class Database:
    def __init__(self):
        self.users = [
            {"id": "user1", "name": "Иван Иванов", "balance": 10000},
            {"id": "user2", "name": "Мария Петрова", "balance": 15000},
        ]
        self.transactions = []

    def get_users(self):
        return self.users

    def add_transaction(self, user_id, order_id, amount, currency):
        for user in self.users:
            if user["id"] == user_id:
                user["balance"] += amount
                self.transactions.append({
                    "user_id": user_id,
                    "order_id": order_id,
                    "amount": amount,
                    "currency": currency
                })

    def get_transactions(self):
        return self.transactions
