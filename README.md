# 📊 Student Performance Analysis

This repository hosts a data analysis project focused on exploring and visualizing factors that influence **student performance in mathematics**.

The core of the project is an interactive web application built with **Streamlit** (`app.py`), which processes and visualizes data from the `student_mat.csv` dataset.

## 🚀 Live Application

You can view and interact with the deployed application directly here:

[**Launch the Streamlit App**](https://lab5advpy-hpzeufffxrmwnpmyrp6exp.streamlit.app/)

-----

## 📂 Repository Contents

| File | Description |
| :--- | :--- |
| `app.py` | The main Python script containing the **Streamlit application logic** and data visualizations. |
| `requirements.txt` | A list of all necessary Python libraries (dependencies) to run the application. |
| `student_mat.csv` | The dataset used for the analysis, containing student demographic, social, and study-related attributes, along with their final math grades. |

-----

## 💻 Local Setup and Run

To run this application on your local machine, follow these steps:

### 1\. Clone the repository

```bash
git clone https://github.com/Poornima030/Student_Performance
cd student-performance
```

### 2\. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies:

```bash
# Create the environment (e.g., named 'perf_env')
python3 -m venv perf_env

# Activate the environment
# On Windows:
.\perf_env\Scripts\activate
# On macOS/Linux:
source perf_env/bin/activate
```

### 3\. Install Required Packages

The project dependencies are listed in the `requirements.txt` file. Use the following command to install all necessary packages:

```bash
pip install -r requirements.txt
```

### 4\. Run the Project

Once all dependencies are installed, you can start the **Streamlit application** from the main script (`app.py`):

```bash
streamlit run app.py
```

This will launch the interactive web application in your default web browser.

-----
