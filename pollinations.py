import requests
from PIL import Image
from io import BytesIO

# No API key required for Pollinations.AI - free to use without signup
# This makes it perfect for educational settings

def generate_image(prompt, width=512, height=512, model="stable-diffusion-v1-5"):
    """
    Generate an image using Pollinations.AI API
    
    Args:
        prompt (str): Text description of the image to generate
        width (int): Width of the output image (default: 512)
        height (int): Height of the output image (default: 512)
        model (str): Model to use for generation (default: stable-diffusion-v1-5)
                     Other options include: "sdxl", "kandinsky", "dalle-mini"
    
    Returns:
        PIL.Image: Generated image
    """
    # Pollinations.AI API endpoint
    api_url = "https://image.pollinations.ai/prompt/"
    
    # URL encode the prompt and create the full request URL
    # Format: {api_url}/{prompt}?width={width}&height={height}&model={model}
    full_url = f"{api_url}{prompt}?width={width}&height={height}&model={model}"
    
    # Send the request
    response = requests.get(full_url)
    
    if response.status_code == 200:
        # Convert the response content to an image
        image = Image.open(BytesIO(response.content))
        return image
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Example usage
if __name__ == "__main__":
    # Define your image prompt
    prompt = "A classroom of diverse teenagers learning about artificial intelligence, digital art style"
    
    # Generate the image
    image = generate_image(
        prompt=prompt,
        width=768,
        height=512,
        model="sdxl"  # Using SDXL for higher quality
    )
    
    if image:
        # Save the generated image
        image.save("pollinations_output.png")
        print(f"Image successfully generated and saved as 'pollinations_output.png'")
        
        # Display the image if running in a notebook environment
        try:
            from IPython.display import display
            display(image)
        except ImportError:
            pass
