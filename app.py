from src.pipelines.pipeline import CompletePipeline
from pywebio.platform.flask import start_server
from src.utils.functions import getConfig
from pywebio.output import *
from pywebio.input import *
from pywebio import config
import os

@config(title = "AutoDataAnalyzer")
def main():
    # Initialize the CompletePipeline instance for data processing
    pipeline = CompletePipeline()
    
    # Create an input group for file uploads and domain entry
    inputData = input_group("Data Upload", 
                            inputs=[
                                file_upload(name="files", label="Upload Files", accept=".csv", multiple=True, placeholder="Drop your CSV files here"),
                                file_upload(name="metadata", label="Upload Metadata", accept=".json", multiple=False, placeholder="Drop your metadata.json here"),
                                input(name="domain", label="Enter the Domain of your dataset")
                            ])
    
    # Load data using the uploaded files and provided metadata/domain context
    with put_loading().style("position: absolute; left: 50%"):
        pipeline.loadData(inputData=inputData["files"], metadata=inputData["metadata"]["content"], domainContext=inputData["domain"])
    
    while True:  # Loop to accept user questions
        question = input(label="Enter your question")
        
        if question == "exit":
            break  # Exit the loop if the user types "exit"
        else:
            with put_loading().style("position: absolute; left: 50%"):
                flag = 0  # Track success of graph generation
                for i in range(5):  # Attempt to generate the graph up to 5 times
                    try:
                        filename, code = pipeline.generateGraph(query=question)  # Generate graph
                    except: 
                        continue  # Skip to the next attempt if an error occurs
                    
                    message = pipeline.pythonRepl.run(code)  # Run the generated code
                    if message == "":
                        flag = 1  # Successful execution
                        break  # Exit loop on success

            # Display results based on success or failure
            if flag == 0:
                put_table([
                    ["Query: ", question],
                    ["Response: ", put_text(f"Encountered error in 5 tries, says: {message}")]
                ])
            else:
                put_table([
                    ["Query: ", question],
                    ["Response: ", put_html(open(filename, "r").read())]  # Display the graph
                ])
            os.remove(filename)  # Clean up generated file

if __name__ == "__main__":
    config = getConfig("config.ini")
    start_server(main, port=config.getint("APPLICATION", "port"), host=config.get("APPLICATION", "host"))