import asyncio
import json
import queue

from send_result_to_django.repository.send_result_to_django_repository import SendResultToDjangoRepository
from send_result_to_django.service.response.send_result_to_django_response import SendResultToDjangoResponse
from template.include.socket_server.utility.color_print import ColorPrinter


class SendResultToDjangoRepositoryImpl(SendResultToDjangoRepository):
    async def requestAiResult(self, userDefinedReceiverFastAPIChannel, userToken):
        temporaryQueueList = []
        userTokenFound = False

        userDefinedReceiverFastAPIChannel.put(json.dumps({"userToken": userToken, "aiResult": 3}))

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

        return SendResultToDjangoResponse.fromValues(userToken, aiResult)
