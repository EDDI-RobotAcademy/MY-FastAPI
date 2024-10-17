import json
import queue

from growth_strategy.repository.growth_strategy_repository import GrowthStrategyRepository


class GrowthStrategyRepositoryImpl(GrowthStrategyRepository):

    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"GrowthStrategyRepositoryImpl getResult()")

        try:
            # 왜 False를 get하지 ?
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"