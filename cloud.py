import requests
from PIL import Image, ImageEnhance
from io import BytesIO

api_token = "your_huggingface_api_token"
headers = {"Authorization": f"Bearer {api_token}"}

prompt = "A vibrant, colorful, and historically accurate painting of Christopher Columbus's arrival in the New World in 1492."

response = requests.post(
    "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4",
    headers=headers,
    json={"inputs": prompt},
)

if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
    image.save("output.png")
else:
    print(f"Error: {response.status_code} - {response.text}")

