import os
from dotenv import load_dotenv
from flask_cors import CORS
from app import create_app

load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
