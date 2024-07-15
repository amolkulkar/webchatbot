# Import the Flask web framework and pandas library
from flask import *
import pandas as pd

# Load the dataset from the uploaded file
file_path = 'chatbot Data.csv'
df = pd.read_csv(r"./chatbot_Data.csv")  # Load the CSV file into a pandas dataframe

# Set pandas options to display all rows
pd.set_option('display.max_rows', None)  # Display all rows in the dataframe

# Get the list of input and output columns dynamically
input_columns = [col for col in df.columns if col.startswith('Input')]  # Get columns starting with 'Input'
output_columns = [col for col in df.columns if col.startswith('Output')]  # Get columns starting with 'Output'

# Convert the dataframe to a list of dictionaries, only including pairs with both input and output
dataset = []  # Initialize an empty list to store the dataset
for index, row in df.iterrows():  # Iterate over each row in the dataframe
    for input_col, output_col in zip(input_columns, output_columns):  # Iterate over input and output columns
        if pd.notna(row[input_col]) and pd.notna(row[output_col]):  # Check if both input and output are not null
            dataset.append({'input': str(row[input_col]), 'output': str(row[output_col])})  # Add to the dataset

# Function to get the response
def get_response(user_input):  # Define a function to get the response
    for pair in dataset:  # Iterate over the dataset
        if pair['input'].lower() == user_input.lower():  # Check if the input matches
            return pair['output']  # Return the output
    return "I'm sorry, I don't understand that."  # Return a default message if no match found

# Create a Flask app
app = Flask(__name__, template_folder='templates')  # Initialize the Flask app

# Define a route for the homepage
@app.route('/')  # Decorator for the homepage route
def hello_world():  # Define a function for the homepage
    return render_template("webpage.html")  # Render the webpage.html template

# Define a route for the chatbot
@app.route('/chatbot', methods=['POST'])  # Decorator for the chatbot route
def interact():  # Define a function for the chatbot
    try:
        user_input = request.form['Statement']  # Get the user input from the form
        response = get_response(user_input)  # Get the response using the get_response function
        print(user_input)  # Print the user input
        print(response)  # Print the response
        return jsonify({'result': response})  # Return the response as JSON
    except Exception as e:  # Catch any exceptions
        return jsonify({'error': str(e)})  # Return the error as JSON

# Run the app
if __name__ == "__main__":  # Check if the script is being run directly
    app.run(debug=True)  # Run the app in debug mode

