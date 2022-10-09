document.getElementById('btn').onclick = function(){
    let temp;
    if(document.querySelector('select').value =='1'){
        temp = document.getElementById('num').value;
        temp = Number(temp);
        temp = toFahrenheit(temp);
        document.getElementById('text').innerHTML = `${temp} Celsius.`;
    }
    else if(document.querySelector('select').value =='2'){
        temp = document.getElementById('num').value;
        temp = Number(temp);
        temp = toCelsius(temp);
        document.getElementById('text').innerHTML = `${temp} Fahrenheit.`;
    }
    else{
        console.log('you need to enter a number.')
    }
}

function toFahrenheit(temp){
    return (temp - 32) * (5/9)

}
function toCelsius(temp){
    return temp * 9 / 5 + 32;
}
