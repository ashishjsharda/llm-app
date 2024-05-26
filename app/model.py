from transformers import pipeline


model = pipeline("text-generation", model="gpt-3.5-turbo")

def generate_text(prompt, max_length=100):
    result = model(prompt, max_length=max_length)
    return result
