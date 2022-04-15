from flask import Flask, render_template, request
from joblib import dump, load
import warnings 
warnings.filterwarnings('ignore')

app = Flask(__name__)

model = load('model.pkl')

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    la = float(request.form.get('la'))
    lb = float(request.form.get('lb'))
    lc = float(request.form.get('lc'))
    va = float(request.form.get('Va'))
    vb = float(request.form.get('Vb'))
    vc = float(request.form.get('Vc'))
    output = model.predict([[la, lb, lc, va, vb, vc]])
    if output == 0:
        return render_template('predict.html', output='Not a Fault')
    elif output == 1:
        return render_template('predict.html', output='Fault')

if __name__  ==  '__main__':
    app.run(debug=True)

