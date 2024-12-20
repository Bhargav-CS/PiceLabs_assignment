# PiceLabs_assignment

This project is a Flask-based web application for fetching and downloading hotel listings in CSV format.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd PiceLabs_assignment
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Endpoints

- `/` - Home page.
- `/fetch` - Fetch hotel listings based on user input.
- `/status` - Check the status of the CSV generation.
- `/check_status` - Endpoint to check the status of the CSV generation.
- `/download` - Download the generated CSV file.
- `/download_csv` - Directly download the CSV file if it exists.

## Templates

- [`templates/index.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FpriceLabs%2FPiceLabs_assignment%2Ftemplates%2Findex.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\priceLabs\PiceLabs_assignment\templates\index.html") - Home page template.
- [`templates/download.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FpriceLabs%2FPiceLabs_assignment%2Ftemplates%2Fdownload.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\priceLabs\PiceLabs_assignment\templates\download.html") - Template for displaying the CSV contents.
- [`templates/status.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FpriceLabs%2FPiceLabs_assignment%2Ftemplates%2Fstatus.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\priceLabs\PiceLabs_assignment\templates\status.html") - Template for displaying the status of the CSV generation.

## License

This project is licensed under the MIT License.