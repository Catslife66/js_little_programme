const textField = document.querySelector('textarea');
const txt = "Click here to auto complete typing.";


textField.addEventListener("click", ()=> {
    let timeId = setInterval(autoType, 50);
    let index = 0;
    let max = txt.length;
    function autoType(){
        index ++;
        textField.style.color = 'grey';
        textField.textContent = txt.slice(0, index);
        if(index >= max){
            clearInterval(timeId);
        }
    }
})


