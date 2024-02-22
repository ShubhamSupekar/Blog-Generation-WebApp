# Welcome to Blog Generation WebApp 🤖
## 1 Introduction:
This web application utilizes Llama 2, an open-source Large Language Model (LLM) developed by Meta for generating blog content across different fields such as data science, research, and general interest topics. In this project, a compressed version of the Llama 2 model is employed to accommodate lower GPU specifications on my laptop. The specific pretrained model file used can be found at [llama-2-7b.ggmlv3.q8_0.bin](https://huggingface.co/TheBloke/Llama-2-7B-GGML/blob/main/llama-2-7b.ggmlv3.q8_0.bin).

This model is a quantized version of the Llama 2 7B generative text model, created by Meta and converted by TheBloke. It uses the GGML format, which is a compressed format for CPU and GPU inference using llama.cpp and other compatible libraries and UIs. The model has 8-bit quantization, meaning it maintains nearly the same accuracy as the original float16 model but is smaller in size and faster to load. However, it also incurs higher resource usage and slower inference than lower-bit quantized models. The model is suitable for various text generation tasks, such as writing stories, poems, essays, code, etc., using prompts or templates.
#### 1.1 what is Llama 2 ? 
Llama 2 is a family of large language models (LLMs) developed and released by Meta, a company formerly known as Facebook. Llama 2 models are trained on a large corpus of public data and can generate natural language for various tasks and applications. Some of the Llama 2 models are also fine-tuned for dialogue using human feedback, making them more engaging and helpful for chatbot users. [Llama 2](https://llama.meta.com/llama2)

## 2 How to run Blog Generation WebApp:
Download pretrained Llama 2 GGM model from [here](https://huggingface.co/TheBloke/Llama-2-7B-GGML/blob/main/llama-2-7b.ggmlv3.q8_0.bin).

Clone project:
```sh
git clone https://github.com/ShubhamSupekar/Blog-Generation-WebApp.git
```
Deactivate the default environment:
```sh
conda deactivate
```
###### Need help with Conda installation? You can find guidance at [click here](https://www.anaconda.com/installation-success?source=installer)

Create new environment:
```sh
conda create -p venv python==3.9 --y
```
Activate new "venv" environment:
```sh
conda activate venv/
```
> The "requirements.txt" file contains the names of all the libraries needed for this project.
Installing all the libraries from requirements.txt file
```sh 
pip install -r .\requirement.txt
```
now to run the WebApp:
```sh
streamlit run app.py
```
