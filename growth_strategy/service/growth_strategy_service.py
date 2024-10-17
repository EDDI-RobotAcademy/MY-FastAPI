from abc import ABC, abstractmethod

class GrowthStrategyService(ABC):

    @abstractmethod
    def requestGrowthStrategyResult(self):
        pass