import gradio as gr

def create_layout():
    layout = {}
    
    gr.Markdown("# CustomPix: Advanced AI-Powered Image Editor")
    
    with gr.Row():
        layout["input_image"] = gr.Image(label="Input Image")
        layout["output_image"] = gr.Image(label="Processed Image")
    
    with gr.Row():
        layout["prompt"] = gr.Textbox(label="Inpainting Prompt", placeholder="Describe the desired change...")
        layout["mask_threshold"] = gr.Slider(minimum=0, maximum=1, value=0.5, label="Mask Threshold")
    
    layout["process_btn"] = gr.Button("Process Image")
    
    gr.Examples(
        examples=[
            ["path/to/example1.jpg", "A serene beach background", 0.6],
            ["path/to/example2.jpg", "A bustling cityscape", 0.4]
        ],
        inputs=[layout["input_image"], layout["prompt"], layout["mask_threshold"]]
    )
    
    return layout
