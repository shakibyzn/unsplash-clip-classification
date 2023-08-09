from clipClassifier import logger
from clipClassifier.entity.config_entity import EvaluationConfig
from pathlib import Path
from PIL import Image
import torch
import numpy as np
import clip
import os
import json


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
        self.model, self.preprocess = None, None
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.labels = ['morning', 'noon', 'afternoon', 'night', 'sunrise or sunset']

    def evaluate(self):
        self.model, self.preprocess = clip.load(self.config.model_name, device=self.device)
        texts = ['A photo taken at ' + label for label in self.labels]
        tokens = clip.tokenize(texts).to(self.device)
        len_images = len(os.listdir(Path(self.config.images_dir)))

        # evaluation
        loggeer.info("evaluation started: reading images")
        for i in range(0, len_images, self.config.batch_size):
            images = [
                self.preprocess(
                    Image.open(os.path.join(Path(self.config.images_dir), img))) \
                        for img in os.listdir(Path(self.config.images_dir))[i:i + self.config.batch_size]
            ]

        images = torch.tensor(np.stack(images)).to(self.device)
        with torch.no_grad():
            logits_per_image, logits_per_text = self.model(images, tokens)
            probs = logits_per_image.softmax(dim=-1).cpu().numpy()

        pred_classes = np.argmax(probs, axis=1)

        # save results as json file, image_name: predicted class
        logger.info(f"evaluation completed")
        data = {k: self.labels[v] for k, v in zip(os.listdir(Path(self.config.images_dir)), pred_classes)}
        with open('predictions.json', 'w') as f:
            json.dump(data, f)