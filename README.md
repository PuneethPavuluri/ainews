# AI NEWS ARTICLE WRITER

This project fine-tuned and utilizes GPT-2 (as GPT-3.5 is not available), Hugging Face Transformers, PyTorch, and Gradio to generate short news articles from provided headlines. The interface is user-friendly and accessible through a web application built with Gradio.

## Concept and Vision: AI News Article Writer
The AI News Article Writer aims to streamline the process of generating news articles by using AI models to produce coherent and relevant content from simple headlines. This tool is particularly beneficial for journalists, bloggers, and content creators who need quick article drafts.

### Key Components:
- **Model**: Fine-tuned GPT-2 using Hugging Face Transformers.
- **Libraries Used**:
  - Hugging Face Transformers
  - PyTorch
  - Gradio
- **Frameworks Considered**:
  - Gradio for the user interface.
- **Datasets Considered**:
  - Datasets from Kaggle and Hugging Face Hub were considered for training. The project uses Hugging Face datasets for fine-tuning.

## Getting Started

### Installation
To get started, install the required libraries:
```bash
!pip install transformers gradio torch
```

### Running the Project
1. Clone the project repository or access it via Google Colab using the following link: [Google Colab Project Link](https://colab.research.google.com/drive/1j3eBAXCaVhRhuqRqJkZh_vZejrsC_sb3?usp=sharing).
2. Install the required libraries as mentioned above.
3. Run the provided code to load the GPT-2 model and tokenizer.
4. Use the Gradio interface to input headlines and generate articles.

### Code Explanation
The provided code snippet loads the GPT-2 model and tokenizer from Hugging Face, defines a function to generate articles from headlines, and sets up a Gradio interface for easy interaction.

```python
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
    inputs = tokenizer.encode(headline, return_tensors='pt')
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
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
```

### Future Work
- Upgrading to GPT-3.5 or GPT-4 for better performance.
- Integrating LangChain for more sophisticated text generation workflows.
- Exploring TensorFlow and FastAPI for deployment and scalability.
- Using additional NLP libraries like spaCy and NLTK for text processing.

This project demonstrates the potential of AI in automating content generation and serves as a foundational step towards more advanced AI writing tools.



You can access and run the project on Google Colab using the following link:
https://colab.research.google.com/drive/1j3eBAXCaVhRhuqRqJkZh_vZejrsC_sb3?usp=sharing
