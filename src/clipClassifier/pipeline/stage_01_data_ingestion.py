from clipClassifier.config.config import ConfigurationManager
from clipClassifier.components.load_data import DataIngestion
from clipClassifier import logger
from pathlib import Path


STAGE_NAME = 'Data Ingestion Stage'

def main():
    # config, params path
    config_path = Path('config/config.yaml')
    params_path = Path('params.yaml')
    # get config
    config = ConfigurationManager(config_path, params_path)
    data_ingestion_config = config.get_data_ingesion_config()
    data_ingestion = DataIngestion(data_ingestion_config)
    data_ingestion.download_images()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed! <<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e