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
    
    year = int(request.form['year'])
    
    km_driven = int(request.form['km_driven'])
    fuel = (request.form['fuel'])
    brand = (request.form['brand'])
    transmission = (request.form['transmission'])
    owner = (request.form['owner'])
    seller_type = (request.form['seller_type'])

    


    lis = {'diesel':0, 'electric':0, 'lpg':0,'petrol':0}

    for i in lis:
        if i== fuel :
            lis[i]= 1
        else :
            lis[i]=0



    

    bran = {'Audi':0, 'BMW':0, 'Chevrolet':0, 'Daewoo':0,
       'Datsun':0, 'Fiat':0, 'Force':0, 'Ford':0,
       'Honda':0, 'Hyundai':0, 'Isuzu':0, 'Jaguar':0,
       'Jeep':0, 'Kia':0, 'Land':0, 'MG':0, 'Mahindra':0,
       'Maruti':0, 'Mercedes-Benz':0, 'Mitsubishi':0,
       'Nissan':0, 'OpelCorsa':0, 'Renault':0, 'Skoda':0,
       'Tata':0, 'Toyota':0, 'Volkswagen':0, 'Volvo':0}

    for i in bran:
        if i== fuel :
            bran[i]= 1
        else :
            bran[i]=0


    Seller = {'Individual':0 ,'Trustmark Dealer':0}

    for i in Seller:
        if i== seller_type :
            Seller[i]= 1
        else :
            Seller[i]=0

    Trans = {'Manual':0}

    for i in Trans:
        if i== transmission :
            Trans[i]= 1
        else :
            Trans[i]=0
    

    owne = {'owner_fourth':0,'owner_second':0,'owner_testdrive':0,'owner_Third':0  }

    for i in owne:
        if i== owner :
            owne[i]= 1
        else :
            owne[i]=0
    
    year1 = [year]
    km_driven1 = [km_driven]
    lis1 = [i for i in lis.values()]
    Seller1 = [i for i in Seller.values()]
    Trans1 = [i for i in Trans.values()]
    bran1 = [i for i in bran.values()]
    owne1 = [i for i in owne.values()]
    
    

    values = year1 + km_driven1 + lis1 + Seller1 + Trans1 + owne1 + bran1
    output = [values]
    predict =  model.predict(output)
    return render_template('index.html', prediction_text='The predicted value is {}'.format(round(predict[0],2)))



if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0':0,port=8080)