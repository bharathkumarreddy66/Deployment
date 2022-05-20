from flask import Flask,request, jsonify, render_template
import numpy as np
import pickle
app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods =['POST'])
def predict():
    init_feat = [int(x) for x in request.form.values()]
    #init_feat[23]= init_feat[23]*init_feat[24]
    final = [(init_feat)]
    print(final)
    predict =  model.predict(final)
    output = predict[0]
    return render_template('index.html', prediction_text='The predicted value is {}'.format(round(output,2)))
if __name__ == "__main__":
    app.run(debug=True)