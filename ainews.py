# Install required libraries
# !pip install transformers gradio torch

# Import libraries
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import gradio as gr

# Load GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Function to generate article from headline
def generate_article(headline, max_length=150):
    # Encode the input headline
    inputs = tokenizer.encode(headline, return_tensors='pt')
    
    # Generate text continuation
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    
    # Decode the generated text
    article = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return article

# Define the Gradio interface
interface = gr.Interface(
    fn=generate_article,
    inputs=gr.Textbox(lines=2, placeholder="Enter news headline here..."),
    outputs="text",
    title="AI News Article Writer",
    description="Generate a short news article based on the provided headline using GPT-2."
)

# Launch the interface
interface.launch()
