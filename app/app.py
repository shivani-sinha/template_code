from flask import Flask, request, Response 
import jsonpickle
import pickle

app = Flask(__name__)
 # Load model
   


@app.route('/api/test', methods=['GET'])
def test():
    # Model code
    response = {'message': 'API hit iimv'}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")



@app.route('/api/testmodel', methods=['GET'])
def process_form():
    #data = request.form
    data = model.predict(33.2)  
    return data


if __name__ == "__main__":
    with open('finalized_model.sav', 'rb') as f:
        print("kp")
        model = pickle.load(f)
    app.run(host="0.0.0.0", port=5000)