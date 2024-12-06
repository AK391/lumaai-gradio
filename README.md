# `lumaai-gradio`

is a Python package that makes it very easy for developers to create machine learning apps that are powered by LumaAI's API.

# Installation

You can install `lumaai-gradio` directly using pip:

```bash
pip install lumaai-gradio
```

That's it! 

# Basic Usage

Just like if you were to use the `lumaai` API, you should first save your LumaAI API key to this environment variable:

```
export LUMAAI_API_KEY=<your token>
```

Then in a Python file, write:

```python
import gradio as gr
import lumaai_gradio

gr.load(
    name='dream-machine',  # Use 'dream-machine' for video, 'photon-1' or 'photon-flash-1' for images
    src=lumaai_gradio.registry,
).launch()
```

Run the Python file, and you should see a Gradio Interface connected to LumaAI!

![ChatInterface](chatinterface.png)

# Customization 

Once you can create a Gradio UI from an LumaAI endpoint, you can customize it by setting your own input and output components, or any other arguments to `gr.Interface`. For example, the screenshot below was generated with:

```py
import gradio as gr
import lumaai_gradio

gr.load(
    name='dream-machine',
    src=lumaai_gradio.registry,
    title='LumaAI-Gradio Integration',
    description="Generate videos and images with LumaAI models.",
    examples=["A serene lake at sunset", "A futuristic cityscape"]
).launch()
```
![ChatInterface with customizations](chatinterface_with_customization.png)

# Composition

Or use your loaded Interface within larger Gradio Web UIs, e.g.

```python
import gradio as gr
import lumaai_gradio

with gr.Blocks() as demo:
    with gr.Tab("Video Generation"):
        gr.load('dream-machine', src=lumaai_gradio.registry)
    with gr.Tab("Image Generation"):
        gr.load('photon-1', src=lumaai_gradio.registry)

demo.launch()
```

# Under the Hood

The `lumaai-gradio` Python library has two dependencies: `lumaai` and `gradio`. It defines a "registry" function `lumaai_gradio.registry`, which takes in a model name and returns a Gradio app.

# Supported Models in LumaAI

The following models are supported:
- `dream-machine`: For video generation
- `photon-1`: For high-quality image generation
- `photon-flash-1`: For fast image generation

-------

Note: if you are getting an authentication error, then the LumaAI API Client is not able to get the API token from the environment variable. This happened to me as well, in which case save it in your Python session, like this:

```python
import os

os.environ["LUMAAI_API_KEY"] = ...
```