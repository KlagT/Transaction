def check_fraud(user_id, amount, db):
    transactions = db.get_transactions()

    # Пример: блокировать транзакции с суммой выше 1 000 000 RUB
    if amount > 1_000_000:
        return False

    # Пример: блокировать более 5 транзакций в минуту
    recent_transactions = [t for t in transactions if t["user_id"] == user_id]
    if len(recent_transactions) > 5:
        return False

    return True
