# Test loss functions

import unittest
import torch

class TestLoss(unittest.TestCase):
    def test_crossentropy(self):
        loss_fn = torch.nn.CrossEntropyLoss()

        dummy_outputs = torch.rand(4, 10)
        dummy_labels = torch.tensor([1, 5, 3, 7])

        loss = loss_fn(dummy_outputs, dummy_labels)
        self.assertTrue(isinstance(loss, torch.Tensor))

