import torch
from .model_struct import CompatibilityNN
    
def ModelLoader():
    ##Loading Model
    model = torch.load('./model/RecommenderModel.pth')
    model.eval()

    ##Returning Model
    return model