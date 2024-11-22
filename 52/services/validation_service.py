def validate_transaction(user_id, amount, currency, db):
    # Проверка существования пользователя
    users = db.get_users()
    if not any(user["id"] == user_id for user in users):
        return False

    # Проверка валюты
    if currency not in ["RUB", "USD", "EUR"]:
        return False

    # Проверка суммы
    if amount <= 0:
        return False

    return True
