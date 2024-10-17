import asyncio
import json
import queue

from ai_to_db_test_point.repository.ai_to_db_test_point_repository import AiToDbTestPointRepository
from ai_to_db_test_point.service.response.ai_to_db_test_point_response import AiToDbTestPointResponse
from template.include.socket_server.utility.color_print import ColorPrinter


class AiToDbTestPointRepositoryImpl(AiToDbTestPointRepository):
    async def requestAiResult(self, userDefinedReceiverFastAPIChannel, userToken):
        temporaryQueueList = []
        userTokenFound = False

        userDefinedReceiverFastAPIChannel.put(json.dumps({"userToken": "test", "aiResult": 3}))

        loop = asyncio.get_event_loop()

        try:
            while True:
                receivedResponseFromSocketClient = await loop.run_in_executor(
                    None, userDefinedReceiverFastAPIChannel.get, False
                )
                data = json.loads(receivedResponseFromSocketClient)

                if data.get("userToken") == userToken:
                    userTokenFound = True
                    aiResult = data.get("aiResult")
                    break

                temporaryQueueList.append(receivedResponseFromSocketClient)

        except queue.Empty:
            ColorPrinter.print_important_message("아직 데이터를 처리 중이거나 요청한 데이터가 없습니다")
            return userTokenFound

        for item in temporaryQueueList:
            await loop.run_in_executor(None, userDefinedReceiverFastAPIChannel.put, item)

        return AiToDbTestPointResponse.fromValues(userToken, aiResult)
