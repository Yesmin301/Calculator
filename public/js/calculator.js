function buttonNum(num){
    document.getElementById("result").value += num
}

function clrResult(){
    document.getElementById("result").value = ""
}
function calculateResut(){
    let num = document.getElementById("result").value
    let result = eval(num)

    document.getElementById("result").value = result
}
function plusMinus(){
    let num = document.getElementById("result").value
    let result = eval(num * - 1)

    document.getElementById("result").value = result
}
function precentage(){
    let num = document.getElementById("result").value
    let result = eval(num / 100)

    document.getElementById("result").value = result
}
