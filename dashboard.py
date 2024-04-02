import gradio as gr
import pandas as pd
import pygwalker as pyg
from pygwalker.api.gradio import PYGWALKER_ROUTE, get_html_on_gradio

with gr.Blocks() as demo:
    df = pd.read_csv('results_full.csv')
    pyg_app = get_html_on_gradio(df, spec="viz_config.json")
    gr.HTML(pyg_app)
    gr.HTML(
        '''
          <h1>Drag & Drop elements to create interative charts. 
          Tutorial is available <a href="https://docs.kanaries.net/graphic-walker/data-viz/create-data-viz">here</a>.</h1>
        '''
      )
 
demo.launch(
    server_name="0.0.0.0",
    server_port=7860,
    show_error=True,  
    app_kwargs={
      "routes": [PYGWALKER_ROUTE]
    }
  )