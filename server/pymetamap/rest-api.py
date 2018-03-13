#!flask/bin/python
import six
from pymetamap import MetaMap

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
mm = MetaMap.get_instance('/opt/public_mm/bin/metamap')

@app.errorhandler(400)
@cross_origin()
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
@cross_origin()
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/annotate', methods=['GET'])
@cross_origin()
def analyze_text():
    text = request.args.get("text")
    concepts,error = mm.extract_concepts(text)
    print(concepts)
    json = jsonify({'annotations':concepts})
    return json

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001, debug=True)
