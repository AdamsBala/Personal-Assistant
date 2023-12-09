from dotenv import load_dotenv
import os
from flask import Flask
from views import views

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, port=3000)
