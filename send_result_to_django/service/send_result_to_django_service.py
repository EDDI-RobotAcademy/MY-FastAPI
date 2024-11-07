from abc import ABC, abstractmethod

from send_result_to_django.service.request.send_result_to_django_request import SendResultToDjangoRequest


class SendResultToDjangoService(ABC):

    @abstractmethod
    async def requestSendCustomStrategyHistory(self, sendResultToDjangoRequest: SendResultToDjangoRequest):
        pass