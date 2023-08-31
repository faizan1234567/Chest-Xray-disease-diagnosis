"""
Utils functions
---------------

chest x ray recognition
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import math
import sklearn
import yaml
from dataset.data import load_dataset
from pretrained_models import get_model

import torch

# device type
device = "cuda" if torch.cuda.is_available() else "cpu"

# get total number of predictions
def get_all_preds(model, loader):
    model.eval()
    with torch.no_grad():
        all_preds = torch.tensor([], device=device)
        for batch in loader:
            images = batch[0].to(device)
            preds = model(images)
            all_preds = torch.cat((all_preds, preds), dim=0)

    return all_preds 





if __name__ == "__main__":
    config_file = "configs/configs.yaml"
    with open(config_file, 'r') as f:
        cfg = yaml.safe_load(f)
    
    data_loader = load_dataset(config_file= cfg, batch_size=32, kind = "test")
    model_name = "resnet18"
    model = get_model(model_name, pretrained = False,
                        num_classes=cfg["DataLoader"]["num_classes"], 
                        weights="logs/lr3e-5_resnet18_cuda.pth")
    preds = get_all_preds(model, data_loader)
    
    
    