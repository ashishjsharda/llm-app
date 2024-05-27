from transformers import pipeline

# Load the model with authentication token during initialization
model = pipeline("text-generation", model="gpt2", use_auth_token="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")

def generate_text(prompt, max_length=100):
    # Generate text using the initialized model
    result = model(prompt, max_length=max_length)
    return result
