from PIL import Image
import numpy as np

class ImageProcessor:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.image_array = np.array(self.image)

    def save_image(self, output_path):
        result_image = Image.fromarray(self.image_array)
        result_image.save(output_path)

    def resize(self, new_width, new_height):
        self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)
        self.image_array = np.array(self.image)

    def crop(self, left, upper, right, lower):
        self.image = self.image.crop((left, upper, right, lower))
        self.image_array = np.array(self.image)

    def rotate(self, angle):
        self.image = self.image.rotate(angle, expand=True)
        self.image_array = np.array(self.image)

    def show(self):
        self.image.show()

def main():
    processor = ImageProcessor('AboutPageBanner.png')

    while True:
        print("Choose an operation:")
        print("1. Resize")
        print("2. Crop")
        print("3. Rotate")
        print("4. Save and Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            new_width = int(input("Enter new width: "))
            new_height = int(input("Enter new height: "))
            processor.resize(new_width, new_height)
            processor.show()

        elif choice == '2':
            left = int(input("Enter left: "))
            upper = int(input("Enter upper: "))
            right = int(input("Enter right: "))
            lower = int(input("Enter lower: "))
            processor.crop(left, upper, right, lower)
            processor.show()

        elif choice == '3':
            angle = float(input("Enter angle to rotate: "))
            processor.rotate(angle)
            processor.show()

        elif choice == '4':
            output_path = input("Enter output path: ")
            processor.save_image(output_path)
            print("Image saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
