# PLDrafter neural network

import torch.nn as nn
import torch.nn.functional as F

class PLDrafterNET(nn.Module):
    def __init__(self) -> None:
        super(PLDrafterNET, self).__init__()
        self.define()

    def define(self):
        self.fc1 = nn.Linear(1, 16)
        self.fc2 = nn.Linear(16, 16)
        self.fc3 = nn.Linear(16, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
