###Library

from flask import Flask,request
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
###Load picklefile
classifier = pickle.load(open('bnknote.pkl','rb'))

###Root Page
@app.route('/')
def welcome():
    return 'Rohan'

@app.route('/predict')

###Create flasgger web
def predict_note_authentication():
    """Let's Authenticate The Bank Notes
    This is using docstrings for specifications.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
    """
    variance =request.args.get('variance')
    skewness =request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    prediction = classifier.predict([[variance,	skewness,	curtosis,	entropy]])
    print(prediction)
    return "The answer is"+str(prediction)

if __name__ == '__main__' :
    app.run(debug=True)
