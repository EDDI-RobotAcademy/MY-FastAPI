from abc import ABC, abstractmethod


class SendResultToDjangoRepository(ABC):
    @abstractmethod
    async def requestAiResult(self, userDefinedReceiverFastAPIChannel, userToken):
        pass

