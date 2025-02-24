import gradio as gr
from src.models.sam_model import load_sam_model, generate_masks
from src.models.inpainting_model import load_inpainting_model, inpaint_image
from src.utils.image_processing import load_image, save_image, preprocess_mask
from src.ui.components import create_mask_editor, create_gallery
from src.ui.layout import create_layout

# Load models
sam_model = load_sam_model()
inpaint_pipe = load_inpainting_model()

def process_image(input_image, prompt, mask, progress=gr.Progress()):
    progress(0, desc="Generating masks")
    masks = generate_masks(input_image, sam_model)
    
    progress(33, desc="Preprocessing mask")
    preprocessed_mask = preprocess_mask(mask)
    
    progress(66, desc="Inpainting")
    result_image = inpaint_image(inpaint_pipe, input_image, preprocessed_mask, prompt)
    
    progress(100, desc="Done")
    return result_image

def custompix_interface():
    with gr.Blocks(css="assets/style.css") as demo:
        layout = create_layout()
        
        mask_editor = create_mask_editor()
        gallery = create_gallery()
        
        layout["process_btn"].click(
            fn=process_image,
            inputs=[layout["input_image"], layout["prompt"], mask_editor],
            outputs=[layout["output_image"], gallery],
            error_message="An error occurred during processing. Please try again."
        )
        
    return demo

if __name__ == "__main__":
    custompix_interface().launch()
