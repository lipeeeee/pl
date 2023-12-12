# Test pytorch tensors
 
import random
import unittest
import torch

class TestTensor(unittest.TestCase):
    def test_adittion(self):
        a = torch.tensor([1, 2, 3])
        b = torch.tensor([1, 2, 3])
        result = a + b == torch.tensor([2, 4, 6])

        [self.assertTrue(x) for x in result]

    def test_shape(self):
        a = torch.empty(2, 2, 3)
        self.assertTrue(a.shape == torch.Size([2, 2, 3]))
        
        x, y, z = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
        b = torch.zeros(x, y, z)
        self.assertTrue(b.shape == torch.Size([x, y, z]))
