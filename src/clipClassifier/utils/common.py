from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
import yaml
from clipClassifier import logger


@ensure_annotations
def read_yaml(path: Path):
    """reads yaml file and returns a ConfigBox

    Args:
        path (Path): path to yaml file

    Returns:
        ConfigBox: ConfigBox
    """
    with open(path) as yaml_file:
        content = yaml.safe_load(yaml_file)
        logger.info(f"yaml file: {path} loaded successfully")
        return content