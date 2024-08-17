from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id).to("cpu")

prompt = "A futuristic cityscape at sunset with flying cars and neon lights"
image = pipe(prompt).images[0]

image.save("output.png")

