import pickle

from tqdm import tqdm, tqdm_notebook
from PIL import Image
from pathlib import Path

from torchvision import transforms

from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch
from torchvision.models import resnet50
from torchvision.models import ResNet50_Weights

import argparse
import warnings



class SmokerClassifier():
    def __init__(self, weights_path: str):
        self.model = resnet50(ResNet50_Weights.DEFAULT)
        self.model.fc = nn.Sequential(
            nn.Linear(2048, 256),
            nn.ReLU(),
            nn.Linear(256, 1)
        )
        
        self.model.load_state_dict(torch.load(weights_path, weights_only=True))
        self.model.eval()
        
        
    def predict(self, images: torch.tensor) -> float:
        with torch.no_grad():
            outp = self.model(images)
            
        probas = torch.sigmoid(outp)
        
        return probas
    
    
    
    
class ImageDataset(Dataset):
    def __init__(self, files):
        super().__init__()
        self.files = sorted(files)
        self.len_ = len(self.files)

    def __len__(self):
        return self.len_

    def load_sample(self, file):
        image = Image.open(file)
        image.load()
        return image

    def __getitem__(self, index):

        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

        x = self.load_sample(self.files[index])
        x = transform(x)

        return x
    
    

def main():
    warnings.filterwarnings("ignore")
    parser = argparse.ArgumentParser(description='Smokers predictor')
    parser.add_argument('indir', type=str, help='Input dir with images')
    parser.add_argument('outpath', type=str, help='Output pickle file for predictions')
    parser.add_argument('weights', type=str, help='Path to model weights')
    args = parser.parse_args()
    
    IM_DIR = Path(args.indir)
    files = sorted(list(IM_DIR.rglob('*.jpg')))
    dataset = ImageDataset(files)
    assert len(dataset) > 0, "Pictures dataset should be not empty"
    
    try:
        model = SmokerClassifier(args.weights)
    except FileNotFoundError:
        print("Incorrect weights path")
        return 1
        
 
    loader = DataLoader(dataset, batch_size=len(dataset), shuffle=False)
    
    for inputs in loader:
        preds = model.predict(inputs).detach().numpy()
        
    res_dict = {}
    for file, pred in zip(files, preds):
        res_dict[str(file)] = pred
    
    try:
        with open(args.outpath, 'wb') as f:
            pickle.dump(res_dict, f)
    except FileNotFoundError:
        print("Incorrect output path")
        return 1
        

        
if __name__ == "__main__":
    main()
        
    
    

   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            