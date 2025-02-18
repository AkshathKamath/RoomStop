import torch
import numpy as np
from .load_model import ModelLoader

def prediction(ip, X):
    model = ModelLoader()

    ip_tensor = torch.tensor(ip, dtype=torch.float32).view(1,-1)

    compatibility_scores = []
    for user in X:
        user_tensor = torch.tensor(user, dtype=torch.float32).view(1, -1)
        combined_profile = torch.cat((ip_tensor, user_tensor), dim=1)

        with torch.no_grad():
            score = model(combined_profile)
            compatibility_scores.append(score.item())
    
    ranked_users = np.argsort(compatibility_scores)[::-1]
    ranked_users.reshape(-1,1)
    return ranked_users[:20]