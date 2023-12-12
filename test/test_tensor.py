# Test pytorch tensors

import torch
import random
import unittest

class TestTensor(unittest.TestCase):
    def test_adittion(self):
        """Basic addition"""
        a = torch.tensor([1, 2, 3])
        b = torch.tensor([1, 2, 3])
        result = a + b == torch.tensor([2, 4, 6])

        [self.assertTrue(x) for x in result]

    def test_shape(self):
        """Test shape sizes"""
        a = torch.empty(2, 2, 3)
        self.assertTrue(a.shape == torch.Size([2, 2, 3]))
        
        x, y, z = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
        b = torch.zeros(x, y, z)
        self.assertTrue(b.shape == torch.Size([x, y, z]))
