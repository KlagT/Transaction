def convert_currency(amount, from_currency, to_currency):
    exchange_rates = {
        "USD": 80,
        "EUR": 90,
        "RUB": 1
    }
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Неизвестная валюта")

    # Конвертация в базовую валюту (RUB), затем в целевую
    amount_in_rub = amount * exchange_rates[from_currency]
    converted_amount = amount_in_rub / exchange_rates[to_currency]
    return round(converted_amount, 2)
