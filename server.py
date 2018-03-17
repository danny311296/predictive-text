from flask import Flask, request, render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_data',methods = ['POST'])
def handle_data():
	inputText = request.form['user_text']
	os.system('python3 markov.py dataset/big/w2_.txt 2');
	return inputText + '\n'
    
if(__name__ == '__main__'):
    app.run(debug=True)
