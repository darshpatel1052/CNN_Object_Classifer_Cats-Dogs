CustomPix: Advanced AI-Powered Image Editor
CustomPix is an advanced AI-powered image editing platform that provides seamless tools for inpainting, object removal, background replacement, and subject substitution. With an intuitive user interface powered by Gradio, CustomPix allows users to manipulate images effortlessly using state-of-the-art machine learning models such as SAM (Segment Anything Model) and Stable Diffusion.

Overview
CustomPix enables users to perform a variety of image editing tasks, including:

Background substitution

Subject substitution

Object removal

Advanced inpainting

The workflow involves uploading an image, selecting objects interactively, refining masks as needed, and providing text prompts to guide AI-based edits. Users can swap out the background or substitute the subject while retaining the original background.

<div align="center"> <img src="./assets/ui_mockup.png" alt="CustomPix UI Mockup: Before and After Comparison" width="800"> </div>
Before Processing
Users upload an input image.

Use the mask editor to draw or erase areas for editing.

Enter text prompts to guide AI-based edits.

After Processing
The processed output image is displayed prominently.

A gallery shows previous edits and allows users to revisit their history.

How It Works
Object Selection:

The Segment Anything Model (SAM) generates masks for objects in the uploaded image.

Users can refine masks manually using the interactive editor.

AI-Powered Inpainting:

Stable Diffusion Inpainting replaces masked areas based on user-provided text prompts.

Real-Time Editing:

All operations are performed in real-time with progress indicators for transparency.

History Viewer:

The gallery component allows users to view past edits and compare results.

How to Execute
1. Clone this repository
bash
git clone https://github.com/yourusername/CustomPix.git
cd CustomPix
2. Create a virtual environment
bash
python -m venv CUSTOMPIX_ENV
Activate the environment:

On Windows:

bash
CUSTOMPIX_ENV\Scripts\activate
On macOS/Linux:

bash
source CUSTOMPIX_ENV/bin/activate
3. Install requirements
bash
pip install -r requirements.txt
4. Run the application
bash
python src/main.py
This will launch the Gradio interface locally at http://127.0.0.1:7860. Open this URL in your browser to access CustomPix.

Examples
Example 1: Background Replacement
<div align="center"> <img src="./assets/example_before.jpg" alt="Before Background Replacement" width="400"> <img src="./assets/example_after.jpg" alt="After Background Replacement" width="400"> </div>
In this example, the user replaced a plain background with a serene beach scene by providing a text prompt: "A serene beach with clear blue skies."

Example 2: Object Removal
<div align="center"> <img src="./assets/object_removal_before.jpg" alt="Before Object Removal" width="400"> <img src="./assets/object_removal_after.jpg" alt="After Object Removal" width="400"> </div>
Here, an unwanted object (a chair) was seamlessly removed from the image using CustomPix's inpainting feature.

Project Structure
text
CustomPix/
├── src/
│   ├── models/
│   │   ├── sam_model.py          # Segment Anything Model integration
│   │   └── inpainting_model.py  # Stable Diffusion Inpainting integration
│   ├── utils/
│   │   ├── image_processing.py  # Image loading, saving, preprocessing utilities
│   │   └── mask_generation.py    # Mask refinement utilities
│   ├── ui/
│   │   ├── components.py         # Gradio UI components like mask editor and gallery
│   │   └── layout.py             # Layout structure for Gradio interface
│   └── main.py                   # Main application logic integrating all components
├── assets/
│   └── style.css                 # Custom styling for Gradio interface
├── data/
│   ├── input/                    # Folder for input images
│   └── output/                   # Folder for processed images
├── configs/
│   └── model_config.yaml         # Configuration file for model paths and parameters
├── requirements.txt              # Dependencies list for Python packages
└── README.md                     # Project documentation file
Contributing
We welcome contributions! If you'd like to contribute to CustomPix, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes and commit them (git commit -m "Add feature").

Push to your branch (git push origin feature-name).

Submit a pull request.
