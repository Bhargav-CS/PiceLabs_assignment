from flask import Flask, request, render_template, send_file, redirect, url_for, jsonify
from flask_executor import Executor
from main import app_flask
import os
import csv
import time

app = Flask(__name__)
executor = Executor(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    # Get user input from the form
    user_params = request.form.to_dict()
    
    # Start background task to generate CSV
    executor.submit(generate_csv, user_params)
    
    return redirect(url_for('status'))

def generate_csv(user_params):
    # Call the main function with user-provided values
    app_flask(user_params)

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/check_status')
def check_status():
    csv_file_path = 'listings.csv'
    if os.path.exists(csv_file_path):
        return jsonify({'status': 'ready'})
    else:
        return jsonify({'status': 'not ready'})

@app.route('/download')
def download():
    # Path to the generated CSV file
    csv_file_path = 'listings.csv'
    
    # Check if the CSV file exists
    if os.path.exists(csv_file_path):
        # Read the CSV file contents
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            csv_contents = list(reader)
        return render_template('download.html', csv_contents=csv_contents)
    else:
        return "CSV file not found", 404

@app.route('/download_csv')
def download_csv():
    csv_file_path = 'listings.csv'
    if os.path.exists(csv_file_path):
        return send_file(csv_file_path, as_attachment=True)
    else:
        return "CSV file not found", 404

if __name__ == '__main__':
    app.run(debug=True)