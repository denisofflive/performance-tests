from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class CreateCardsGatewayHTTPClient(TypedDict):
    """
    Структура данных для создания виртуальной и физической карт.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: CreateCardsGatewayHTTPClient) -> Response:
        """
         Создание новой виртуальной карты.

        :param request: Словарь с данными новой виртуальной карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreateCardsGatewayHTTPClient) -> Response:
        """
        Создание новой физической карты.

        :param request: Словарь с данными новой физической карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
