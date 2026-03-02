import time

# Импортируем библиотеку httpx для отправки HTTP-запросов
import httpx

# Формируем уникальный email пользователя, используя текущее время,
# чтобы избежать дублирования адресов при многократном запуске скрипта
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Отправляем POST-запрос на создание нового пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)

# Получаем JSON-данные из ответа сервера
create_user_response_data = create_user_response.json()

# Формируем payload для открытия депозитного счета, используя ID вновь созданного пользователя
open_deposit_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}

# Открываем депозитный счёт, отправляя POST-запрос с указанным userID
open_deposit_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-deposit-account",
    json=open_deposit_account_payload
)

# Парсим ответ сервера в виде JSON
open_deposit_account_response_data = open_deposit_account_response.json()

# Выводим содержимое ответа и статус-код HTTP
print("Open deposit account response:", open_deposit_account_response_data)
print("Open deposit account status code:", open_deposit_account_response.status_code)
