import sys
import modelsetup
import gradio as gr
import dataprocessing

# Load and process the data
text_chunks = dataprocessing.load_and_process_data("data/")

# Configure the model and its components
qa = modelsetup.setup_model_and_components("data/model/mistral-7b-instruct-v0.1.Q5_K_M.gguf", text_chunks)

# while True:
#     user_input = input(f"Input Prompt: ")
#     if user_input == 'exit':
#         print('Exiting')
#         sys.exit()
#     if user_input == '':
#         continue
#     result = qa({'query': user_input})
#     print(f"Answer: {result['result']}")
# Define function to respond to queries
def respond_to_query(query):
    result = qa({'query': query})
    return result['result']

# Create Gradio interface
interface = gr.Interface(
    fn=respond_to_query,
    inputs=gr.Textbox(label="Query", placeholder="Enter your query"),
    outputs=gr.Textbox(label="Response"),
    theme="gradio",
    css="""
    .gradio-container {
      background: rgb(225, 180, 199);
      padding-top: 50px; /* Adjust as needed */
    }
    .gradio-container title {
        font-size: 24px;
        color: #007bff;
        text-align: center;
        margin-bottom: 20px;
    }
    button {
      background: #C4698F;
      color: #ffffff;
    }

    """,
)

# Launch the Gradio interface
interface.launch(share=True)