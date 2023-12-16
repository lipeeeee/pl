from model import PLModel
import torch
import pl_drafter 

net = pl_drafter.PLDrafterNET()
print(net.forward(torch.tensor(1)))
