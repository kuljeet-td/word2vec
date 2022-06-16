from flask import Flask
from word2vec.api.endpoints import word2vec

application = Flask(__name__)
application.config["JSON_SORT_KEYS"] = False

application.register_blueprint(word2vec)


if __name__ == "__main__":
    application.run(debug=False)
