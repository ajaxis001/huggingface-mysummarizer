from transformers import pipeline
import gradio as gr 

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.inputs.Textbox(placeholder="Enter text block to summarize", lines=4)
    output_text = gr.outputs.Textbox()
    gr.Interface(fn=predict, inputs=textbox, outputs=output_text)

demo.launch() 
