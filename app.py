from flask import Flask, render_template,request
import pickle

app = Flask(__name__, template_folder = 'template')

model = pickle.load(open('model.pkl', 'rb'))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Mobil = (request.form['Mobil'])
    Jenis = (request.form['Jenis'])
    Tipe = int(request.form['Tipe'])
    Jarak = int(request.form['Jarak'])
    Tahun = int(request.form['Tahun'])
    Gearshift = int(request.form['Gearshift'])
    BBM = int(request.form['BBM'])
    
    predict_list = [[Mobil, Jenis, Tipe, Jarak, Tahun, Gearshift, BBM]]
    prediction = model.predict(predict_list)
    output = round(prediction[0])

    return render_template('index.html', prediction_text='Harga Mobil adalah Rp.{}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)
    