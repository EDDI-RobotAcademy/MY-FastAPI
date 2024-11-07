import os
import sys

from api.django_http_client import DjangoHttpClient
from send_result_to_django.repository.send_result_to_django_repository_impl import SendResultToDjangoRepositoryImpl
from send_result_to_django.service.request.send_result_to_django_request import SendResultToDjangoRequest
from send_result_to_django.service.send_result_to_django_service import SendResultToDjangoService

from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class SendResultToDjangoServiceImpl(SendResultToDjangoService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__sendResultToDjangoRepository = SendResultToDjangoRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def requestSendCustomStrategyHistory(self, sendResultToDjangoRequest: SendResultToDjangoRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()

        ColorPrinter.print_important_message("requestToCheckMultipleUserTestPoint()")

        sendResultToDjangoResponse = await self.__sendResultToDjangoRepository.requestAiResult(
            userDefinedReceiverFastAPIChannel,
            sendResultToDjangoRequest.toUserToken()
        )

        print(f"sendResultToDjangoResponse: {sendResultToDjangoResponse}")
        success = await DjangoHttpClient.post("/custom_strategy_history/save", sendResultToDjangoResponse.json())

        return success


