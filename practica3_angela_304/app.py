from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect(url_for('servidor'))

@app.route('/servidor', methods=['GET', 'POST'])
def servidor():
    resultado = None
    error = None

    if request.method == 'POST':
        numero1 = float(request.form.get('numero1'))
        numero2 = float(request.form.get('numero2'))
        operacion = request.form.get('operacion')

        if operacion == 'suma':
            resultado = numero1 + numero2
        elif operacion == 'resta':
            resultado = numero1 - numero2
        elif operacion == 'multiplicacion':
            resultado = numero1 * numero2
        elif operacion == 'division':
            if numero2 == 0:
                error = 'No es posible dividir entre cero.'
            else:
                resultado = numero1 / numero2

    return render_template('servidor.html', resultado=resultado, error=error)

@app.route('/cliente')
def cliente():
    return render_template('cliente.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
