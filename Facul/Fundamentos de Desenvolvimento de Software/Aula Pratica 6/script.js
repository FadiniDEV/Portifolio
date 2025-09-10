const campo1 = document.querySelector("#campo1");
const campo2 = document.querySelector("#campo2");
const operacao = document.querySelector("#operacao");
let resposta = document.querySelector("#resposta");
 

operacao.addEventListener("change", calcular);
campo1.addEventListener("input", calcular);
campo2.addEventListener("input", calcular);


function calcular(){
    const valor1 = parseFloat(campo1.value);
    const valor2 = parseFloat(campo2.value);
    const op = operacao.value;

    if (isNaN(valor1) || isNaN(valor2)){
        resposta.classList.add = "problema";
        resposta.innerHTML = "Por favor, insira números válidos nos dois campos.";
        setTimeout(() => {
            resposta.classList.remove = "problema";
            resposta.innerHTML = "";
            }, 3000);
    }
    else if (op === "Somar"){
        resposta.innerHTML = valor1 + valor2;
    }
    else if (op === "Subtrair"){
        resposta.innerHTML = valor1 - valor2;
    }
    else if (op === "Multiplicar"){
        resposta.innerHTML = valor1 * valor2;
    }
    else if (op === "Dividir"){
        if (valor2 === 0){
            resposta.innerHTML = "Erro: Divisão por zero não é permitida.";
        }
        else {
            resposta.innerHTML = valor1 / valor2;
        }
    }
    else {
        resposta.innerHTML = "Operação inválida. Por favor, selecione uma operação válida.";
    }
}



/*Daqui pra baixo é o codigo do botão dolorido*/

let botao = document.querySelector("#botao");

botao.style.background = "blue";
botao.style.border = "1px solid black";

let dolorido = false;
let contaClick = 0;

botao.addEventListener("mouseover", e =>{
    if (!dolorido)
        botao.style.background = "green";
});

botao.addEventListener("mouseout", e =>{
    if (!dolorido)
        botao.style.background = "blue";
});

botao.addEventListener("click", e =>{
    
    contaClick++;
    if (contaClick >= 2){
        botao.style.background = "red";
        botao.innerHTML = "Doeu";
        dolorido = true;
        alert("Vai catuca tua mae fidaputa! Me dxa em paz!");
    }
    else{
        botao.innerHTML = "Por favor, pare! Ta doendo!";
    }
});