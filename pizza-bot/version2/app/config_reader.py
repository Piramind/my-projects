import configparser
from dataclasses import dataclass
from config import *

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config

    return Config(
        tg_bot=TgBot(
            token=[tg_bot]
        )
    )
