"""MNIST-A Dataset module for parallel DataLoader support on macOS.

This module exists because Python's multiprocessing with 'spawn' method
(default on macOS and Windows) requires classes to be importable from
a proper module, not defined in __main__ (Jupyter notebooks).
"""

import numpy as np
from PIL import Image
from torch.utils.data import Dataset


class MNISTA_Dataset(Dataset):
    """Custom Dataset for MNIST-A (Arabic Handwritten Digits)"""

    def __init__(self, images, labels, transform=None):
        self.images = images
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        img = self.images[idx].reshape(28, 28)
        # Fix orientation: flip first, then rotate with k=3
        img = np.fliplr(img).copy()  # Horizontal flip
        img = np.rot90(img, k=1).copy()  # Rotate 90 degrees

        # Convert to PIL for transforms
        img = Image.fromarray(img)

        if self.transform:
            img = self.transform(img)

        # Convert to Python int to ensure proper DataLoader collation
        label = int(self.labels[idx])
        return img, label
