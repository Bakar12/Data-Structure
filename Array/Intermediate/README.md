# Image Processing Project

This project implements various image processing operations in Python using the PIL and numpy libraries.

## Files

- `ImageProcessing.py`: This file contains the `ImageProcessor` class, which implements the image processing operations.

## Usage

To use the `ImageProcessor` class, create an instance and use the various methods to perform operations on the image.

```python
processor = ImageProcessor('AboutPageBanner.png')
processor.resize(new_width, new_height)
processor.show()
processor.crop(left, upper, right, lower)
processor.rotate(angle)
processor.save_image(output_path)
```
## Testing

To run the application, navigate to the Array/Intermediate directory and run the ImageProcessing.py file with Python:

```
python ImageProcessing.py
```
## License
This project is licensed under the terms of the MIT license.

