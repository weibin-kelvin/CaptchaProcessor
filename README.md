# Captcha Processor

## Description

Captcha Processor is a Python tool that processes and identifies CAPTCHA characters using image processing techniques with OpenCV and NumPy. It reads a set of images and corresponding text files, processes the image regions, and compares them against stored character data to predict the CAPTCHA output.

## Exploratory Data Analysis - Key observations which were subsequently used in approach

* "the font and spacing is the same each time" - Checked and confirmed that the location to each of the 5 characters is the same across all 25 files. Coded logics to extract character at expected location. 
* "the background and foreground colors and texture, remain largely the same" - Checked and confirmed that characters shading are different even for each character or background. Observed that the RGB are either more than 40 or less than 40. Use 40 as the threshold. Coded logics to remove texture on character and background so that it becomes black and white only without background. 
* "there is no skew in the structure of the characters" - Checked and confirmed that after processing of the character into B/W and without background, they are identical. 
* output21.txt is not available in link hence skipping the use of input21. used as part of testing to check if code works

## Table of Contents

* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
* [Methods and Functions](#methods-and-functions)
* [File Structure](#file-structure)
* [Example Usage](#example-usage)
* [License](#license)

## Problem Formulation and Approach

The objective of this project is to develop a CAPTCHA processing tool that can accurately identify characters in CAPTCHA images by comparing segmented regions of the image with stored character data. The problem is framed as an image processing and pattern recognition task, where the following steps were implemented:

1. **Data Collection and Input Structure:** Images named `input01.jpg` to `input24.jpg`  and corresponding text files `output01.txt` to `output24.txt` were utilized as inputs.

2. **Image Processing:** The images are divided into five character regions, each processed as a binary matrix using thresholding to isolate character pixels.

3. **Data Storage and Comparison:** The processed character matrices are stored in a dictionary, allowing for direct comparison of newly processed characters with stored data.

4. **Prediction and Output:** The tool processes new images, applies the same segmentation and thresholding, and compares the resulting matrices to predict CAPTCHA output.

## Installation

Ensure you have Python 3.x installed. Install the necessary libraries using the following command:

```bash
pip install opencv-python-headless matplotlib numpy
```

## Usage

To use the `CaptchaProcessor` class, follow these steps:

1. Prepare the given training input folder containing the CAPTCHA images named as `input01.jpg` to `input24.jpg`.
2. Prepare the given training output folder containing the corresponding text files named as `output01.txt` to `output24.txt`. (observed to be without output21.txt)
3. Instantiate the class with the input and output folder paths.
4. Call the `process_images()` method to process and compare the images.
5. Use the `__call__()` method to predict the CAPTCHA output from a new image.

## Methods and Functions

* `__init__(self, input_folder, output_folder)`: Initializes the class with the input and output folder paths.
* `process_images(self)`: Processes all images and compares the processed data with the stored characters.
* `get_coordinates(self, index)`: Returns the coordinates for the character regions.
* `predict_image(self, image_path)`: Processes a new image for prediction.
* `compare_predictions(self, save_path)`: Compares predictions and saves the CAPTCHA output.
* `__call__(self, image_path, save_path='captcha_output.txt')`: Executes the prediction and comparison workflow.

## File Structure

```
Project Folder
│   CaptchaProcessor.py
│   README.md
│
├───input
│   ├── input01.jpg
│   ├── input02.jpg
│   └── ...
│
└───output
    ├── output01.txt
    ├── output02.txt
    └── ...
```

## Example Usage

```python
from CaptchaProcessor import CaptchaProcessor

input_folder = './input'
output_folder = './output'

captcha_processor = CaptchaProcessor(input_folder, output_folder)
captcha_processor.process_images()

# Predict from a new image
captcha_processor('input/sample_image.jpg', 'captcha_output.txt')
```

## License

MIT License
