from flask import Flask, render_template, url_for, request
import itertools

app = Flask(__name__)


@app.route('/')
def home():


    return render_template('index.html')


@app.route('/list', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        req = request.form
        str = req['string']
        a = str.split(" ")
        x = 100
        word_list = []
        for e in range(x):
            for i in itertools.permutations(a, e):
                list = ''.join(i)
                word_list.append(list)





    return render_template('list.html', wl = word_list)

app.run(debug=True)


