import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

class CaptchaProcessor:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.data_dict = {}
        self.predict_data_dict = {}

    def process_images(self):
        for i in range(0, 25):
            if i == 21:
                continue

            input_file = os.path.join(self.input_folder, f"input{i:02}.jpg")
            output_file = os.path.join(self.output_folder, f"output{i:02}.txt")

            image = cv2.imread(input_file)
            if image is None:
                print(f"Failed to load image: {input_file}")
                continue

            for j in range(5):
                x1, y1, x2, y2 = self.get_coordinates(j)
                clean_char = np.where(image[y1:y2, x1:x2] > 40, 255, 0)

                try:
                    with open(output_file, 'r', encoding='utf-8') as file:
                        characters = file.read()
                        if j < len(characters):
                            char = characters[j]
                            if char in self.data_dict:
                                if np.array_equal(self.data_dict[char], clean_char):
                                    print(f"{char}: same")
                                else:
                                    print(f"{char}: different")
                            else:
                                self.data_dict[char] = clean_char
                except FileNotFoundError:
                    print(f"File not found: {output_file}")

    def get_coordinates(self, index):
        coordinates = [
            (5, 11, 13, 21),
            (14, 11, 22, 21),
            (23, 11, 31, 21),
            (32, 11, 40, 21),
            (41, 11, 49, 21)
        ]
        return coordinates[index]

    def predict_image(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to load image: {image_path}")
            return

        for i in range(5):
            x1, y1, x2, y2 = self.get_coordinates(i)
            clean_char = np.where(image[y1:y2, x1:x2] > 40, 255, 0)
            self.predict_data_dict[f"Pred_{i}"] = clean_char

    def compare_predictions(self, save_path):
        captcha_output = ""
        for key1, values1 in self.predict_data_dict.items():
            for key2, values2 in self.data_dict.items():
                if np.array_equal(values1, values2):
                    print(f"Match found: {key2}")
                    captcha_output += key2

        output_file_path = save_path
        with open(output_file_path, "w") as file:
            file.write(captcha_output)

    def __call__(self, image_path, save_path='captcha_output.txt'):
        self.predict_image(image_path)
        self.compare_predictions(save_path)
