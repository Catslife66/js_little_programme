document.getElementById('btn').onclick = function(){
    let num;
    if(document.getElementById('unit').value == '1'){
        num = document.getElementById('num').value;
        num = Number(num);
        num = toMile(num);
        document.getElementById('show').innerHTML = `${num}`;
        document.getElementById('x-unit').value = '2';
    }
    else if(document.getElementById('unit').value == '2'){
        num = document.getElementById('num').value;
        num = Number(num);
        num = toKilometer(num);
        document.getElementById('show').innerHTML = `${num}`;
        document.getElementById('x-unit').value = '1';
    }

}

function toKilometer(num){
    return num * 1.609

}
function toMile(num){
    return num * 0.621
}