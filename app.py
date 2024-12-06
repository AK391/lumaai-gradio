import gradio as gr
import lumaai_gradio

gr.load(
    name='dream-machine',
    src=lumaai_gradio.registry,
).launch()