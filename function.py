from PIL import Image

import torch
import torch.nn.functional as F
from torchvision import transforms

MODEL = torch.load('transfer_model')
IMG_TRANSFORMS = transforms.Compose([transforms.Resize((64,64)), transforms.ToTensor()])
CLASS_NAMES = ['Саркосцифа алая', 'Лисичка настоящая', 'Масленок обыкновенный', ' Подберезовик',
               'Белый гриб', 'Подосиновик', 'Опёнок']

def predict_models(path: str):
    img = Image.open(path)
    img = IMG_TRANSFORMS(img)
    img = torch.unsqueeze(img, 0)
    MODEL.eval()

    prediction = F.softmax(MODEL(img), dim=1)
    prediction = prediction.argmax()
    return CLASS_NAMES[prediction]