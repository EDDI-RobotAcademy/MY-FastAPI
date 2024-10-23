import os.path
import sys

from fastapi.middleware.cors import CORSMiddleware

import colorama

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from ai_to_db_test_point.controller.ai_to_db_test_point_controller import aiToDbTestPointRouter
from growth_strategy.controller.growth_strategy_controller import growthStrategyRouter
from send_result_to_django.controller.send_result_to_django_controller import sendResultToDjangoRouter
from user_defined_initializer.init import UserDefinedInitializer

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.deep_learning.controller.deep_learning_controller import deepLearningRouter
from template.dice.controller.dice_controller import diceResultRouter
from template.system_initializer.init import SystemInitializer
from template.task_manager.manager import TaskManager
from template.include.socket_server.initializer.init_domain import DomainInitializer

DomainInitializer.initEachDomain()
SystemInitializer.initSystemDomain()
UserDefinedInitializer.initUserDefinedDomain()

app = FastAPI()

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deepLearningRouter)
app.include_router(diceResultRouter)
app.include_router(growthStrategyRouter)
app.include_router(aiToDbTestPointRouter)
app.include_router(sendResultToDjangoRouter)

if __name__ == "__main__":
    colorama.init(autoreset=True)

    TaskManager.createSocketServer()
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))

