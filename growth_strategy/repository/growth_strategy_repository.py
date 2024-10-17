from abc import ABC, abstractmethod


class GrowthStrategyRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass