from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect(url_for('triangulo'))

@app.route('/triangulo', methods=['GET', 'POST'])
def triangulo():
    area = None
    perimetro = None

    if request.method == 'POST':
        base = float(request.form['base'])
        altura = float(request.form['altura'])
        lado1 = float(request.form['lado1'])
        lado2 = float(request.form['lado2'])
        lado3 = float(request.form['lado3'])

        area = (base * altura) / 2
        perimetro = lado1 + lado2 + lado3

    return render_template(
        'triangulo.html',
        area=area,
        perimetro=perimetro
    )
if __name__ == '__main__':
    app.run(debug=True)