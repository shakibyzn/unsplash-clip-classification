import os
from pathlib import Path
from src.clipClassifier.utils.common import read_yaml
from src.clipClassifier.entity.config_entity import DataIngestionConfig, EvaluationConfig


class ConfigurationManager:
    def __init__(self, config_path: Path, params_path: Path):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

    def get_data_ingesion_config(self):
        return DataIngestionConfig(**self.config["data_ingestion"])

    def get_evaluation_config(self):
        return EvaluationConfig(
            images_dir=self.config["evaluation"]["images_dir"],
            model_path=self.config["evaluation"]["model_path"],
            model_name=self.config["evaluation"]["model_name"],
            image_size=self.params["IMAGE_SIZE"],
            batch_size=self.params["BATCH_SIZE"])
