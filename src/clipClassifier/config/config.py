import os
from pathlib import Path
from src.clipClassifier.utils.common import read_yaml
from src.clipClassifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_path: Path, params_path: Path):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        
    def get_data_ingesion_config(self):
        return DataIngestionConfig(**self.config["data_ingestion"])