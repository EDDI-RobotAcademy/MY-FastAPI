from abc import ABC, abstractmethod

from ai_to_db_test_point.service.request.ai_to_db_test_point_request import AiToDbTestPointRequest


class AiToDbTestPointService(ABC):

    @abstractmethod
    async def requestAiResultToDbTestPoint(self, aiToDbTestPointRequest: AiToDbTestPointRequest):
        pass