from gensim.models import KeyedVectors
from flask import request, jsonify, Blueprint

word2vec = Blueprint("w2v_app", __name__)


def load_w2v_model(path="word2vec/data"):
    """
    load the data files
    """
    filename = '{}/GoogleNews-vectors-negative300.bin.gz'.format(path)
    model_ = KeyedVectors.load_word2vec_format(filename, binary=True)
    return model_


model = load_w2v_model()


@word2vec.route('/word2vec/', methods=['POST'])
def return_vector():
    try:
        payload_data_ = request.get_json()
        word = payload_data_['word']
        if word in model.vocab:
            vector = model.get_vector(word=word.strip())
            return jsonify(
                {'data': vector.tolist(), 'status_code': 200})
        else:
            return jsonify(
                {'message': '404 Not Found',
                 'status': '404'}
            )
    except Exception as e:
        return jsonify({'error': str(e)})
