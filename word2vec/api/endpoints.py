import logging

import numpy as np
from flask import request, jsonify, Blueprint
from gensim.models import KeyedVectors

word2vec = Blueprint("w2v_app", __name__)
logging.getLogger().setLevel(logging.INFO)


def load_w2v_model(path="/data"):
    """
    load the data files
    """
    filename = f'{path}/GoogleNews-vectors-negative300.bin.gz'
    model_ = KeyedVectors.load_word2vec_format(filename, binary=True)
    return model_


model = load_w2v_model()
logging.info("Model has been loaded...")


@word2vec.route('/get_vector', methods=['GET'])
def return_vector():
    try:
        word = request.args.get('word')
        arr = np.array([model.get_vector(word=word.strip()) for word in word.split(" ")]).mean(axis=0)
        if arr.size < 300:
            return jsonify({'data': np.zeros(shape=(300,)).tolist()}), 200
        return jsonify({'data': arr.tolist()}), arr
    except Exception as e:
        logging.error(e)
        return jsonify(
            {'message': 'Something went wrong, please try again later'}), 500
