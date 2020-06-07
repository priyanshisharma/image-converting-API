# image-converting-API

This contains API that converts the input image, to its Base 64 string and MD5 hash and returns the same along with storing it in the database.

## Setup and run

1. Create a virtual environment with Python3.7: `virtualenv env -p python3.7`. If you dont have `python3.7` yet then you can install it with:
    1. linux(ubuntu/debian) - `sudo apt install python3.7`
    2. windows - Download installer from https://www.python.org/downloads/release/python-370/.
2. Activate the virtual environment: `source env/bin/activate`
3. Install all the dependencies in `requirements.txt` file: `pip install -r requirements.txt`
4. Migrate the migrations: `python manage.py migrate`
5. Run the app: `python manage.py runserver`
6. Navigate to http://localhost:8000 in your browser
7. When you are done using the app, deactivate the virtual environment: `deactivate`