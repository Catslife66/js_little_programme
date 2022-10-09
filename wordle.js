const answer = ['D', 'A', 'N', 'D', 'Y'];
const guesses = 6;
const inputSquares = document.querySelectorAll('.square');
const keyBoard = document.querySelectorAll('.letter');

const userInput = [];
const inputLength = 30;

let userGuess = 0;
let okToInput;
let checkingStage = false;
let enterPressed = false;
let guess = [];
let index = -1;
let winning = false;


window.addEventListener("keypress", (event) => {
    if(!enterPressed && !checkingStage){
        index ++
        let inputLetter = event.key
        userInput.push(inputLetter)
        inputSquares[index].innerHTML = inputLetter
        inputSquares[index].classList.add('write')
        keyBoardChange(event)
    }

    if(index >= 4){
        checkingStage = true
    }
    
})


function keyBoardChange(event){
    for(i=0;i<keyBoard.length;i++){
        if(keyBoard[i].textContent == event.key){
            keyBoard[i].classList.add('pressed')
        }
    }
}

function fillSquare(index, inputLetter){
    inputSquares[index].innerHTML = inputLetter
    inputSquares[index].classList.add('write')
}


// function fillSquare() {
//     keyBoard.forEach((letter) => {
//         letter.addEventListener("keypress", (event) => {
//             let inputLetter = event.key
//             userInput.push(inputLetter)
//             console.log(inputLetter)
//             inputSquares.forEach((square) => {
//                 square.textContent = inputLetter
//             })
//         })
//     })
// }


// function guessWord(){
//     window.addEventListener("keypress", (event) => {
//         if(guess.length < 5){
//             guess.push(event.key)
//         }

//         //check answer
//         if(guess[0] == answer[0] && 
//             guess[1] == answer[1] &&
//             guess[2] == answer[2] && 
//             guess[3] == answer[3] && 
//             guess[4] == answer[4] && 
//             guess[5] == answer[5]){
//                 winning = true
//             } else {
//                 winning = false
//                 userGuess 
//                 console.log()
//             }
//     })
// }
