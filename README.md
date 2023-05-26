# Langchain Demo Project

This demo project showcases how to use Langchain to interact with a large data source using PySpark with a Streamlit frontend. The project focuses on analyzing an eCommerce behavior dataset sourced from Kaggle.

## Dataset

- The dataset used for this project is the [eCommerce Behavior Data from a Multi-Category Store](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store) available on Kaggle. Please download the dataset and place it in the project directory.


### Prerequisites

- [Python 3.8](https://www.python.org/downloads/) or higher
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) (for creating the environment)
- [Git](https://git-scm.com/downloads) (for cloning the repository)


## Getting Started

To execute the project, please follow the instructions below:

1. Clone the project repository from GitHub:

   ```bash
   git clone https://github.com/rohan-mudaliar/langchian-demo.git

2. Change into the project directory:

    ```bash
    cd langchian-demo

3.  Create a new Conda environment with Python 3.8:

    ```bash
    conda create --name langchain-demo python=3.8

4. Activate the newly created Conda environment:
    ```bash
    conda activate langchain-demo

5. Install the project dependencies using requirements.txt:

    ```bash
    pip install -r requirements.txt


# Running the Application

1. Start the Streamlit application by executing the following command:

 
    streamlit run app.py

2. Once the application is running, open your web browser and navigate to the provided URL (usually http://localhost:8501).
3. Use the available prompts to interact with the application and query the eCommerce behavior dataset. For example:
- To count the number of records in the electronics database, enter the following prompt:


    count number of records in electronics database

- To retrieve the order ID in the electronics database that has the highest price, use the following prompt:


    give me order ID in electronics database that has the highest price

# Project Structure

The project repository contains the following files and directories:

- `app.py`: The main entry point of the application, responsible for launching the Streamlit frontend and handling user prompts.
- `langchain.py`: The Langchain module, which interacts with the eCommerce behavior dataset using PySpark.
- `data`: A directory where you should place the downloaded eCommerce behavior dataset CSV file (not included in the repository due to size constraints).
- `requirements.txt`: A file specifying the Python dependencies required for running the project.
- `README.md`: This README document, providing instructions and information about the project.

# Contributing

Contributions to this project are welcome! If you find any issues or would like to propose enhancements, please submit a pull request or open an issue on the [GitHub repository](https://github.com/your-repo).
