from src.clipClassifier.components.evaluation import Evaluation
from src.clipClassifier.config.config import ConfigurationManager
from src.clipClassifier import logger
from pathlib import Path

STAGE_NAME = 'Evaluation Stage'

def main():
    # config, params path
    config_path = Path('config/config.yaml')
    params_path = Path('params.yaml')
    # get config
    config = ConfigurationManager(config_path, params_path)
    evaluation_config = config.get_evaluation_config()
    evaluation = Evaluation(evaluation_config)
    evaluation.evaluate()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed! <<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e