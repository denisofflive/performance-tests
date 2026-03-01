import time

import httpx  # Импортируем библиотеку HTTPX

# Данные для создания пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем запрос на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Выводим полученные данные пользователя
print("Create user response:", create_user_response_data)
print("Status Code:", create_user_response.status_code)
user_id = create_user_response.json()["user"]["id"]
print("User ID:", user_id)

# Выполняем запрос на открытие аккаунта c использованием USER ID
post_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account/",
                                   json={"userId": create_user_response.json()["user"]["id"]})

# Выводим полученные данные
print("Open Account response:", post_account_response)
print("Status Code:", post_account_response.status_code)
