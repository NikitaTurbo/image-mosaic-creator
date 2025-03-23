# Image Mosaic Creator

<img src="https://img.shields.io/github/languages/top/NikitaTurbo/image-mosaic-creator?color=red" alt="language" />

A tool for creating image mosaics by replacing small sections of an image with similar images from a dataset.

## Features
- Divides an input image into small tiles
- Calculates the average color of each tile
- Finds the most similar image from a dataset for each tile
- Creates a mosaic by replacing tiles with matching images

## Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/NikitaTurbo/image-mosaic-creator.git
cd image-mosaic-creator
pip install -r requirements.txt
```

## Usage
1. Prepare a dataset of images in a folder named "dataset"
2. Run the script and input the name of your source image (without extension)
3. The script will create a mosaic version of your image

```python
python main.py
```


## How It Works
The script divides the input image into small tiles (default size: 10x10 pixels). For each tile, it calculates the average color and finds the most similar image from the dataset based on color similarity. It then replaces each tile with the corresponding dataset image, creating a mosaic effect.

## Output Example
<p align="center">
  <img width="100%" src="https://github.com/NikitaTurbo/image-mosaic-creator/blob/main/original.jpg" alt="Original Image">
  <img width="100%" src="https://github.com/NikitaTurbo/image-mosaic-creator/blob/main/mosaic.jpg" alt="Mosaic Image">
</p>

## Configuration
You can modify these variables in the script:
- `SIZE`: Size of each tile in pixels
- `FOLDER_NAME`: Name of the folder containing dataset images
- `NUMBER_OF_IMAGES`: Number of images in your dataset
- `IMAGE_EXTENSION`: File extension of your images