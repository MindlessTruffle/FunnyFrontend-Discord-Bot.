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
import json

load_dotenv()

genai.configure(api_key=os.environ["GEMENI_API_KEY"])

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

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

def createImage(prompt, imagenum):
    model_id1 = "dreamlike-art/dreamlike-diffusion-1.0"

    image = pipe(prompt).images[0]

    # Convert the image to a numpy array
    image_np = np.array(image)

    # Convert to PIL Image
    image_pil = Image.fromarray(image_np)

    # Create the folder if it doesn't exist
    Path("ai_images").mkdir(parents=True, exist_ok=True)

    # Save the image to the folder
    image_pil.save(f"ai_images/result_image{imagenum}.png")

def youtubeSearch(terms, amt):
    return YoutubeSearch(terms, max_results=1).to_dict()

def checkLink(string):
    word_list = ["png", "jpg", "jpeg", "webp"] # NNOTE: ADD IMAGE CONVERSION FOR STUFF LIKE avif
    link = str(string)
    for i in word_list:
        check = i + "?"
        if check in link:
            return True
    else:
        return False

canvasColorDict = {
    "red": (255, 0, 0),
    "lightred": (255, 153, 153),
    "darkred": (139, 0, 0),

    "green": (0, 255, 0),
    "lightgreen": (144, 238, 144),
    "darkgreen": (0, 100, 0),

    "blue": (0, 0, 255),
    "lightblue": (173, 216, 230),
    "darkblue": (0, 0, 139),

    "yellow": (255, 255, 0),
    "lightyellow": (255, 255, 153),
    "darkyellow": (205, 205, 0),

    "cyan": (0, 255, 255),
    "lightcyan": (224, 255, 255),
    "darkcyan": (0, 139, 139),

    "magenta": (255, 0, 255),
    "lightmagenta": (255, 119, 255),
    "darkmagenta": (139, 0, 139),

    "orange": (255, 165, 0),
    "lightorange": (255, 204, 153),
    "darkorange": (255, 140, 0),

    "purple": (128, 0, 128),
    "lightpurple": (204, 153, 255),
    "darkpurple": (75, 0, 130),

    "pink": (255, 192, 203),
    "lightpink": (255, 182, 193),
    "darkpink": (199, 21, 133),

    "brown": (165, 42, 42),
    "lightbrown": (210, 180, 140),
    "darkbrown": (139, 69, 19),

    "gray": (128, 128, 128),
    "lightgray": (211, 211, 211),
    "darkgray": (105, 105, 105),

    "white": (255, 255, 255),
    "black": (0, 0, 0),

    "gold": (255, 215, 0),
    "silver": (192, 192, 192),

    "cream": (255, 253, 208),
    "banana": (255, 225, 53),
    "peach": (255, 218, 185),
    "maroon": (128, 0, 0),
    "zaffre": (0, 20, 168),
    "olive": (128, 128, 0),
    "lightgreen": (162, 232, 89),
}

def ping_to_id(input_string):
    if len(input_string) < 3:
        return "Input string must have at least 3 characters"
    else:
        return input_string[2:-1]
    
# print("GPU Enabled: " + str(torch.cuda.is_available()))
