function obtenerValores() {
    let a = parseFloat(document.getElementById("a").value);
    let b = parseFloat(document.getElementById("b").value);
    let c = parseFloat(document.getElementById("c").value);
    let d = parseFloat(document.getElementById("d").value);
    let e = parseFloat(document.getElementById("e").value);
    return [a, b, c, d, e];
}

function suma() {
    let [a, b, c, d, e] = obtenerValores();
    document.getElementById("resultado").innerText = a + b + c + d + e;
}

function promedio() {
    let [a, b, c, d, e] = obtenerValores();
    document.getElementById("resultado").innerText = (a + b + c + d + e) / 5;
}

function volumen() {
    let [a, b, c, d, e] = obtenerValores();
    document.getElementById("resultado").innerText = a * b * c * d * e;
}

function operacion() {
    let [a, b, c, d, e] = obtenerValores();
    document.getElementById("resultado").innerText = (a + b) * (c + d) - e;
}

function polinomio() {
    let [a, b, c, d, e] = obtenerValores();
    let x = 2;
    document.getElementById("resultado").innerText =
        a*x**4 + b*x**3 + c*x**2 + d*x + e;
}
