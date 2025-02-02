# -*- coding: utf-8 -*-
"""Sentence Generation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CCrgBdR2KiN0N7L8RXBaLrEZ7QJjFP4k
"""

!pip install -q gradio
!pip install -q git+https://github.com/huggingface/transformers.git

import gradio as gr
import tensorflow as tf
from transformers import TFGPT2LMHeadModel,GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained ("gpt2")
model = TFGPT2LMHeadModel.from_pretrained ("gpt2" ,pad_token_id=tokenizer.eos_token_id)

def generate_text(input_Prompt):
    input_ids = tokenizer.encode(input_Prompt, return_tensors='tf')
    beam_output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, early_stopping=False)
    output = tokenizer.decode(beam_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return ".".join(output.split(".")[:-1]) + "."

output_text = gr.Textbox()

gr. Interface(generate_text,"textbox", output_text, title="GPT-2",

description="OpenAI's GPT-2 is an unsupervised language model that \ can generate coherent text. Go ahead and input a sentence and see what it completes \ it with! Takes around 20s to run.").launch()