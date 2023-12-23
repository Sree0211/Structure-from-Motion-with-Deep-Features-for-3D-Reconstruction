import numpy as np
import os

from tqdm import tqdm
import time
import hydra
from omegaconf import DictConfig
from pathlib import Path

import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.autograd import Variable

from PIL import Image

# ResNet model for feature extraction
class ResNetFeatureExtractor(nn.Module):
    def __init__(self):
        super(ResNetFeatureExtractor, self).__init__()
        resnet = models.resnet18()
        
        # Remove the classification head
        self.resnet_features = nn.Sequential(*list(resnet.children())[:-1])

    def forward(self, x):
        return self.resnet_features(x)

def feature_extractor(img_path, model, transform):
    image = Image.open(img_path).convert('RGB')
    image = transform(image).unsqueeze(0)
    image = Variable(image)

    model.eval()

    # Extract features
    with torch.no_grad():
        features = model(image)

    return features.squeeze().numpy()


@hydra.main(config_path=".", config_name="config.yaml", version_base="1.2")
def main(cfg:DictConfig) -> None:
    dataset_name = cfg.dataset
    print("The dataset for our project is {}".format(dataset_name),"\n")
    
    # Perform Image Transforms
    resnet_model = ResNetFeatureExtractor()
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    images_root = cfg.aachen_daynight.images_root
    print("Images root folder: {}".format(images_root),"\n")

    # Extract from features from all files in the specified folder
    all_features = []
    files = os.listdir(images_root)
    
    for file in tqdm(files, desc="Processing files", unit="file"):
        features = feature_extractor(os.path.join(images_root,file),resnet_model,transform)
        all_features.append(features)

    output_path = cfg.save_roots.feature_data
    np.save(os.path.join(output_path,"resnet_features.npy"),np.array(all_features))
    
    
    
if __name__ == "__main__":
    start = time.time()
    
    print("===== FEATURE EXTRACTION START =====")
    main()
    print("===== FEATURE EXTRACTION DONE! =====")
    
    end = time.time()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("\nAll done in {:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
