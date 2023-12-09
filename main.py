from dotenv import load_dotenv
import os
from flask import Flask
from landing import landing

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)
app.register_blueprint(landing, url_prefix="/landing")

if __name__ == '__main__':
    app.run(debug=True, port=3000)
