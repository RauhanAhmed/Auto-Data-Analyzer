# AutoDataAnalyzer

**AutoDataAnalyzer** is a cutting-edge tool designed to automate the process of data ingestion, analysis, and visualization using powerful AI/ML models and interactive pipelines. This application provides a seamless experience for uploading datasets, querying data, and generating insightful visualizations.

---

## Features

- **Interactive Data Analysis**: Upload datasets and metadata, then query for insights.
- **Automated Visualization**: Generates high-quality, interactive Plotly visualizations.
- **Custom Query Handling**: Uses advanced LLMs (Llama 3.1-70B) for natural language query processing.
- **Pipeline Integration**: End-to-end processing via LangChain and other robust frameworks.
- **Dockerized Deployment**: Easy setup with Docker support.
- **CI/CD Workflow**: Fully automated CI/CD pipeline using GitHub Actions.

---

## Table of Contents

1. [Directory Structure](#directory-structure)
2. [Technical Details](#technical-details)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Screenshots](#screenshots)
7. [License](#license)

---

## Directory Structure

```
RauhanAhmed-Auto-Data-Analyzer/
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
├── app.py
├── requirements.txt
├── setup.py
├── params.yaml
├── config.ini
├── Dockerfile
├── LICENSE
└── src/
    ├── components/
    │   ├── queryChainBuilder.py
    │   ├── dataIngestion.py
    │   ├── __init__.py
    │   └── codeGenerator.py
    ├── __init__.py
    ├── pipelines/
    │   ├── __init__.py
    │   └── pipeline.py
    └── utils/
        ├── logger.py
        ├── exceptions.py
        ├── __init__.py
        └── functions.py
```

---

## Technical Details

### Tools and Frameworks

- **Programming Language**: Python 3.10
- **Web Framework**: Flask
- **Interactive Interface**: PyWebIO
- **Visualization**: Plotly
- **Large Language Model**: Llama 3.1-70B
- **Task Management**: LangChain (including experimental and community modules)
- **Deployment**: Docker
- **CI/CD**: GitHub Actions

### Key Components

#### `app.py`
- Entry point of the application.
- Hosts the PyWebIO-based interactive interface.
- Integrates the `CompletePipeline` for data ingestion and query processing.

#### `src/components/queryChainBuilder.py`
- Builds a LangChain query processing chain.
- Loads configurations from YAML and INI files.
- Utilizes `ChatGroq` for natural language processing.

#### `params.yaml`
- Contains system-level prompts and rules for data handling and visualization generation.

#### `Dockerfile`
- Defines the container environment for easy deployment.

#### `.github/workflows/ci-cd.yaml`
- Automates CI/CD processes, including Docker image building and deployment via webhooks.

---

## Requirements

- Python 3.10
- Docker
- Dependencies listed in `requirements.txt`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RauhanAhmed/AutoDataAnalyzer.git
   cd AutoDataAnalyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. (Optional) Build and run using Docker:
   ```bash
   docker build -t autodataanalyzer .
   docker run -p 7860:7860 autodataanalyzer
   ```

---

## Usage

1. Start the application by running `app.py` or the Docker container.
2. Upload your CSV files and metadata.
3. Enter your query in natural language.
4. View the generated visualization and export as needed.
5. Type `exit` to terminate the application.

---

## Screenshots

![Upload and Query](./demo/uploadData.png)

![Visualization Output](./demo/visualizationOutput.png)

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Author

Developed by [**Rauhan Ahmed Siddiqui**](https://github.com/RauhanAhmed/Auto-Data-Analyzer).