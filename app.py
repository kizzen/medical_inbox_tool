from flask import Flask, render_template, request, jsonify
import pandas as pd
import random

app = Flask(__name__, template_folder='templates', static_folder='static')

# Load the CSV file
df = pd.read_csv('data_generation/data/df.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    question = transcription = None
    answers_wc = answers_nc = ""
    index = None  # initialize index variable

    # If form is submitted
    if request.method == 'POST':
        index = random.choice(df.index.tolist())
        question = df.iloc[index]['questions']
        transcription = df.iloc[index]['transcription']

    return render_template('index.html', index=index, question=question, transcription=transcription, answers_wc=answers_wc, answers_nc=answers_nc)

@app.route('/get_answers', methods=['POST'])
def get_answers():
    index = int(request.form.get('index'))
    answers_wc = df.iloc[index]['answers_wc']
    answers_nc = df.iloc[index]['answers_nc']
    return jsonify({'answers_wc': answers_wc, 'answers_nc': answers_nc})

if __name__ == '__main__':
    app.run(debug=True)
