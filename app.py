
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    hasil=0
    a=0
    b=0
    if request.method == 'POST':
        a = eval(request.form['a'])
        b = eval(request.form['b'])
        hasil = 1/2 * a * b
    return render_template('index.html', hasil=hasil, a=a, b=b)
if __name__ == '__main__':
    app.run(debug=True)