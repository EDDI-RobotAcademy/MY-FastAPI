from abc import ABC, abstractmethod
from typing import List, Optional


class AiToDbTestPointRepository(ABC):
    @abstractmethod
    async def requestAiResult(self, userDefinedReceiverFastAPIChannel, userToken):
        pass

