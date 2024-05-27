import unittest
from PIL import Image
import numpy as np
from pandas.conftest import cls

from ..ImageProcessing import ImageProcessor

class TestImageProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = ImageProcessor('ContactUs.png')

    def test_resize(self):
        original_size = cls.processor.image.size
        new_width, new_height = 100, 100
        cls.processor.resize(new_width, new_height)
        self.assertEqual(cls.processor.image.size, (new_width, new_height))
        cls.processor.resize(*original_size)  # Reset to original size

    def test_crop(self):
        original_size = cls.processor.image.size
        cls.processor.crop(10, 10, original_size[0] - 10, original_size[1] - 10)
        self.assertEqual(cls.processor.image.size, (original_size[0] - 20, original_size[1] - 20))
        cls.processor.image = Image.open('ContactUs.png')  # Reset to original image

    def test_rotate(self):
        cls.processor.rotate(90)
        rotated_size = cls.processor.image.size
        self.assertNotEqual(rotated_size, (cls.processor.image_array.shape[1], cls.processor.image_array.shape[0]))
        cls.processor.image = Image.open('ContactUs.png')  # Reset to original image

if __name__ == '__main__':
    unittest.main()

