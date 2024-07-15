# Flask Chatbot Application

This is a simple Flask-based chatbot application that uses a dataset from a CSV file to provide responses to user inputs.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Customization](#customization)
- [Acknowledgements](#acknowledgements)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-repo/flask-chatbot.git
    cd flask-chatbot
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
    
        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:
    
        ```bash
        source venv/bin/activate
        ```

4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Place your dataset:**

    Ensure that your CSV file (e.g., `chatbot_Data.csv`) is placed in the same directory as `app.py`.

2. **Run the Flask application:**

    ```bash
    python app.py
    ```

3. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

4. **Interact with the chatbot:**

    - Type your message in the input field.
    - Click the "Submit" button to send your message.
    - The chatbot will respond based on the dataset provided.

## Project Structure

flask-chatbot/
│
├── app.py # Main Flask application
├── templates/
│ └── webpage.html # HTML template for the chatbot interface
├── chatbot_Data.csv # Dataset for the chatbot
├── requirements.txt # List of Python dependencies
└── README.md # This README file

## Dependencies

- Flask
- pandas

To install the dependencies, run:

```bash
pip install -r requirements.txt



