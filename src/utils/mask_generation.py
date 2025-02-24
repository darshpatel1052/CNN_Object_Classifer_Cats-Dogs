import numpy as np

# Generate a refined mask based on user input (e.g., additional points)
def refine_mask(original_mask, additional_points):
    refined_mask = original_mask.copy()
    for point in additional_points:
        refined_mask[point[1], point[0]] = 1  # Set pixel at (x, y) to 1
    return refined_mask

# Invert a mask (for subject substitution)
def invert_mask(mask):
    inverted = np.logical_not(mask)
    return inverted.astype(np.uint8) * 255  # Convert back to uint8 format
