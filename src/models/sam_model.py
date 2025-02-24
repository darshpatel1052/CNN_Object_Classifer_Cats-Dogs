from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import torch

# Load the SAM model
def load_sam_model(model_path="sam_vit_h_4b8939.pth"):
    sam = sam_model_registry["vit_h"](checkpoint=model_path)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    sam.to(device)
    return SamAutomaticMaskGenerator(sam)

# Generate masks for an input image
def generate_masks(image, model):
    masks = model.generate(image)
    return masks
