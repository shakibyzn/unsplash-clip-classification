from  clipClassifier.utils.common import read_yaml
import torch
from pathlib import Path
import clip
from PIL import Image


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.model_name = read_yaml(Path("config/config.yaml"))["evaluation"]["model_name"]
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.labels = ['morning', 'noon', 'afternoon', 'night', 'sunrise or sunset']

    def predict(self):
        # load model
        model, preprocess = clip.load(self.model_name, device=self.device)
        image = preprocess(Image.open(self.filename)).unsqueeze(0)
        texts = ['A photo taken at ' + label for label in self.labels]
        tokens = clip.tokenize(texts).to(self.device)

        # evaluation
        with torch.no_grad():
            logits_per_image, logits_per_text = model(image, tokens)
            probs = logits_per_image.softmax(dim=-1).numpy()
            pred_cls = self.labels[probs.argmax()]

        return [{"image": pred_cls}]
