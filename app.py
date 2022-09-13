


from flask import Flask,jsonify,render_template,request
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))

app= Flask(__name__)


@app.route('/')
def home():
    print('hello')
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    cgpa=eval(request.form.get('cgpa'))
    iq=eval(request.form.get('iq'))
    profile_score=eval(request.form.get('profile_score'))

    # prediction
    result=model.predict(np.array([cgpa,iq,profile_score]).reshape(1,3))

    if result[0] == 1:
        result = 'placed'
    else:
        result = 'not placed'
    


   

    return str(result)

    






if __name__== '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)