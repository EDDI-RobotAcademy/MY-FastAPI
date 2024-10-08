from abc import ABC, abstractmethod

class GrowthStrategyRepository(ABC):

    @abstractmethod
    def fetch_growth_strategy(self, prompt: str):
        pass