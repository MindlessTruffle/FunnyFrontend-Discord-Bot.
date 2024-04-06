import google.generativeai as genai
import musicpy as mp
from youtube_search import YoutubeSearch

from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os
import torch
import numpy as np
from torchvision.utils import save_image, make_grid
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMENI_API_KEY"])

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def generate_content(prompt):
    try:
        convo = model.start_chat(history=[])
        convo.send_message(prompt)
        response = convo.last.text
        # Truncate the response if it exceeds 2000 characters
        if len(response) > 2000:
            response = response[:2000]
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"

def all_capitalizations(word):
    if not word:
        return ['']
    first = word[0]
    rest = word[1:]
    lower_first = [first.lower() + tail for tail in all_capitalizations(rest)]
    upper_first = [first.upper() + tail for tail in all_capitalizations(rest)]
    return lower_first + upper_first

def createImage(prompt, imagenum):
    model_id1 = "dreamlike-art/dreamlike-diffusion-1.0"

    image = pipe(prompt).images[0]

    # Convert the image to a numpy array
    image_np = np.array(image)

    # Convert to PIL Image
    image_pil = Image.fromarray(image_np)

    # Create the folder if it doesn't exist
    Path("downloaded_images").mkdir(parents=True, exist_ok=True)

    # Save the image to the folder
    image_pil.save(f"downloaded_images/result_image{imagenum}.png")

def youtubeSearch(terms, amt):
  return YoutubeSearch(terms, max_results=1).to_dict()

print("GPU Enabled: " + str(torch.cuda.is_available()))
