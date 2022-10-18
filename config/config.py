import string
from platform import node
from typing import List

import yaml
from pydantic import BaseModel


class AppConfig(BaseModel):
    addr: str
    port: int
    nodes: List[str]


def read(file_name):
    defaultConfig: AppConfig = {
        "addr": "0.0.0.0",
        "port": 8000,
        "nodes": ["http://localhost:5051"],
    }

    with open(file_name, "r") as f:
        yamlConfig: AppConfig = yaml.load(f, Loader=yaml.FullLoader) or {}

    config: AppConfig = {**defaultConfig, **yamlConfig}

    return config
