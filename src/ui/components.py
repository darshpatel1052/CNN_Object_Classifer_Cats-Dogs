import gradio as gr

def create_mask_editor():
    return gr.Image(tool="sketch", label="Mask Editor", brush_radius=10)

def create_gallery():
    return gr.Gallery(label="Editing History", show_label=False, elem_id="gallery").style(grid=2, height="auto")
