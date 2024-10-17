import os
import sys

from growth_strategy.repository.growth_strategy_repository_impl import GrowthStrategyRepositoryImpl
from growth_strategy.service.growth_strategy_service import GrowthStrategyService

from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class GrowthStrategyServiceImpl(GrowthStrategyService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__growthStrategyRepository = GrowthStrategyRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository


    def requestGrowthStrategyResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__growthStrategyRepository.getResult(userDefinedReceiverFastAPIChannel)