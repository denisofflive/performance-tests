# Импортируем библиотеку httpx для отправки HTTP-запросов и модуль time для генерации уникального email адреса
import time
import httpx

# Формируем payload для создания нового пользователя
# Используем уникальное значение времени для email, чтобы каждый раз создавать новый уникальный адрес
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Отправляем POST-запрос на создание пользователя и получаем ответ
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)

# Преобразуем тело ответа в JSON и сохраняем данные пользователя
create_user_response_data = create_user_response.json()

# Формируем payload для открытия кредитной карты с ID пользователя, полученного на предыдущем этапе
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]  # Получаем id пользователя из предыдущего ответа
}

# Открываем кредитную карту для пользователя путем отправки POST-запроса
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)

# Сохраняем данные открывшейся кредитной карты
open_credit_card_account_response_data = open_credit_card_account_response.json()

# Формируем payload для совершения покупки
# Используем первую карту из списка карточек аккаунта и добавляем категорию платежа ("taxi")
make_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,  # Сумма операции
    "cardId": open_credit_card_account_response_data["account"]["cards"][0]["id"],  # Берём первый доступный cardID
    "category": "taxi",
    "accountId": open_credit_card_account_response_data["account"]["id"]  # Идентификатор счета
}

# Совершаем покупку путём отправки POST-запроса
make_purchase_operation_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=make_purchase_operation_payload
)

# Получаем данные совершенной операции
make_purchase_operation_response_data = make_purchase_operation_response.json()

# Запрашиваем чек операции GET-методом, передавая ID операции
get_operation_receipt_response = httpx.get(
    f"http://localhost:8003/api/v1/operations/operation-receipt/{make_purchase_operation_response_data['operation']['id']}"
)

# Преобразуем полученный ответ в JSON и выводим его вместе с кодом статуса
get_operation_receipt_response_data = get_operation_receipt_response.json()

# Выводим итоговые данные операции и статус её выполнения
print('Get operation receipt response:', get_operation_receipt_response_data)
print('Get operation receipt status code:', get_operation_receipt_response.status_code)
