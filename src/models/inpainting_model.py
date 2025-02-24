from diffusers import StableDiffusionInpaintPipeline
import torch

# Load the inpainting model
def load_inpainting_model(model_name="stabilityai/stable-diffusion-2-inpainting"):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionInpaintPipeline.from_pretrained(model_name)
    pipe.to(device)
    return pipe

# Perform inpainting on an image
def inpaint_image(pipe, image, mask, prompt):
    result = pipe(prompt=prompt, image=image, mask_image=mask).images[0]
    return result
