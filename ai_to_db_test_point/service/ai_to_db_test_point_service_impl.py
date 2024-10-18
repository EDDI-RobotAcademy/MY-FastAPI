import os
import sys

from ai_to_db_test_point.repository.ai_to_db_test_point_repository_impl import AiToDbTestPointRepositoryImpl
from ai_to_db_test_point.service.ai_to_db_test_point_service import AiToDbTestPointService
from ai_to_db_test_point.service.request.ai_to_db_test_point_request import AiToDbTestPointRequest

from api.django_http_client import DjangoHttpClient

from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class AiToDbTestPointServiceImpl(AiToDbTestPointService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__aiToDbTestPointRepository = AiToDbTestPointRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def requestAiResultToDbTestPoint(self, aiToDbTestPointRequest: AiToDbTestPointRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()

        ColorPrinter.print_important_message("requestToCheckMultipleUserTestPoint()")

        aiToDbTestPointResponse = await self.__aiToDbTestPointRepository.requestAiResult(
            userDefinedReceiverFastAPIChannel,
            aiToDbTestPointRequest.toUserToken()
        )

        success = await DjangoHttpClient.post("/ai2db/testpoint", aiToDbTestPointResponse.json())

        return success


