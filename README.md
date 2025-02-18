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

### Project Workflow
The project workflow involves fine-tuning GPT-2 on a dataset from Hugging Face, loading the model and tokenizer, and using a Gradio interface for user interaction. Headlines are processed to generate coherent articles, demonstrating the capabilities of fine-tuned language models.

### Future Work
- Upgrading to GPT-3.5 or GPT-4 for better performance.
- Integrating LangChain for more sophisticated text generation workflows.
- Exploring TensorFlow and FastAPI for deployment and scalability.
- Using additional NLP libraries like spaCy and NLTK for text processing.

This project demonstrates the potential of AI in automating content generation and serves as a foundational step towards more advanced AI writing tools.

