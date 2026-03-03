import time
import httpx

# Создание нового пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Шаг 2. Открытие кредитного счёта
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]

}
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)
open_credit_card_account_response_data = open_credit_card_account_response.json()

print("Open credit account response:", open_credit_card_account_response_data)
print("Open credit account status code:", open_credit_card_account_response.status_code)

# Шаг 2. Совершить операцию покупки (purchase)

create_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "category": "taxi",
    "cardId": open_credit_card_account_response_data['account']['cards'][0]['id'],
    "accountId": open_credit_card_account_response_data["account"]["id"]

}

create_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation",
                                                json=create_purchase_operation_payload)
operation_id = create_purchase_operation_response.json()["operation"]["id"]

print("Open purchase operation response:", operation_id)
print("Open purchase operation status code:", create_purchase_operation_response.status_code)

# Выполняем запрос на получение операции по ID
get_operation_receipt_id_response = httpx.get(
    f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}"
)
get_operation_receipt_id_response_data = get_operation_receipt_id_response.json()

# Выводим полученные данные
print("Get operation receipt response:", get_operation_receipt_id_response_data)
print("Get operation receipt Status Code:", get_operation_receipt_id_response.status_code)
