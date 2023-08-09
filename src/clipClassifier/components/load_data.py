import pandas as pd
from clipClassifier import logger
from clipClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path
import os
import requests
from PIL import Image


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_images(self):
        # download images
        if not os.path.exists(Path(self.config.images_dir)):
            os.makedirs(Path(self.config.images_dir))

        # read first 20 rows
        df = pd.read_csv(self.config.data_dir, sep='\t', nrows=20)
        for img_url in df['photo_image_url']:
            img_path = os.path.join(Path(self.config.images_dir), img_url.split('/')[-1] + '.jpg')
            response = requests.get(img_url)
            if response.status_code == 200:
                # save image
                with open(img_path, 'wb') as f:
                    f.write(response.content)

        logger.info(f"All images downloaded successfully")


