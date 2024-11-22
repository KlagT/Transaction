from flask import Flask, render_template, request, redirect, url_for, flash
from services.validation_service import validate_transaction
from services.fraud_detection_service import check_fraud
from services.logging_service import log_transaction
from services.valute_convertor_service import convert_currency
from system_containers import Database
import uuid

app = Flask(__name__)
app.secret_key = "secret_key_for_flask"

# Инициализация базы данных
db = Database()


@app.route('/')
def index():
    users = db.get_users()
    return render_template('index.html', users=users)


@app.route('/submit_transaction', methods=['POST'])
def submit_transaction():
    user_id = request.form['user_id']
    amount = float(request.form['amount'])
    currency = request.form['currency']

    # Генерация идентификатора заказа
    order_id = str(uuid.uuid4())

    # Проверка транзакции
    if not validate_transaction(user_id, amount, currency, db):
        flash("Ошибка: Проверьте данные транзакции.")
        return redirect(url_for('index'))

    # Проверка на мошенничество
    if not check_fraud(user_id, amount, db):
        flash("Транзакция заблокирована из-за подозрений в мошенничестве.")
        return redirect(url_for('index'))

    # Конвертация валюты
    converted_amount = convert_currency(amount, currency, "RUB")

    # Сохранение транзакции
    db.add_transaction(user_id, order_id, converted_amount, "RUB")
    flash(f"Транзакция успешно выполнена. Сумма: {converted_amount} RUB")

    # Логирование
    log_transaction(user_id, order_id, converted_amount, "RUB")

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
