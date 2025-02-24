from PIL import Image
import numpy as np

# Load an image from a file path
def load_image(image_path):
    return Image.open(image_path).convert("RGB")

# Save an image to a file path
def save_image(image, output_path):
    image.save(output_path)

# Convert a mask to binary format (if needed)
def preprocess_mask(mask):
    binary_mask = np.array(mask) > 128  # Thresholding for binary mask
    return Image.fromarray(binary_mask.astype(np.uint8) * 255)
