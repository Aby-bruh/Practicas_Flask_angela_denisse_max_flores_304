const formulario = document.getElementById('formCalculadora');
const resultadoTexto = document.getElementById('resultado');
const errorTexto = document.getElementById('error');

formulario.addEventListener('submit', function(event) {
    event.preventDefault();

    const numero1 = parseFloat(document.getElementById('numero1').value);
    const numero2 = parseFloat(document.getElementById('numero2').value);
    const operacion = document.getElementById('operacion').value;

    let resultado;
    let error = '';

    if (operacion === 'suma') {
        resultado = numero1 + numero2;
    } else if (operacion === 'resta') {
        resultado = numero1 - numero2;
    } else if (operacion === 'multiplicacion') {
        resultado = numero1 * numero2;
    } else if (operacion === 'division') {
        if (numero2 === 0) {
            error = 'No es posible dividir entre cero.';
        } else {
            resultado = numero1 / numero2;
        }
    }

    if (error !== '') {
        errorTexto.textContent = error;
        errorTexto.classList.remove('oculto');
        resultadoTexto.classList.add('oculto');
    } else {
        resultadoTexto.textContent = 'Resultado: ' + resultado;
        resultadoTexto.classList.remove('oculto');
        errorTexto.classList.add('oculto');
    }
});
