from flask import Flask, jsonify

from resources.games import games

# import models.py
import models

from flask_cors import CORS

DEBUG=True
PORT=8000


app = Flask(__name__)

CORS(games, origins=['http://localhost:3000', ])
app.register_blueprint(games, url_prefix='/games')













if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
