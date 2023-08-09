from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    data_dir: Path
    images_dir: Path


@dataclass(frozen=True)
class EvaluationConfig:
    images_dir: Path
    model_path: Path
    model_name: str
    image_size: list
    batch_size: int