const answer = ['D', 'A', 'N', 'D', 'Y'];
const guesses = 6;
const inputSquares = document.querySelectorAll('.square');
const keyBoard = document.querySelectorAll('.letter');

const userInput = [
    ['', '', 'A', '', ''],
    ['', 'F', '', '', ''],
    ['F', 'F', 'F', 'F', 'G'],
    ['', '', 'C', '', ''],
    ['D', '', '', '', ''],
    ['', '', '', '', ''],
];

let userGuess = 0;
let okToInput;
let guess = [];
let winning = false;

inputSquares.forEach((square, index)=> {
    square.addEventListener('click', () => {
        checkToInput(index)
        
    })
})


function checkToInput(index) {
    let rowNum = Math.floor(index / 5);
    //check first line is ok to input
    if(rowNum == 0){
        if(index == 0 && userInput[rowNum][index] == '') {
            okToInput = true
        }else if (index > 0 && userInput[rowNum][index] == '' && userInput[rowNum][index-1] != ''){
            okToInput = true
        }else {
            okToInput = false
        }
    }
    // check the rest of lines are ok to input
    else if(rowNum > 0){
        if(userInput[rowNum-1].includes('')){
            okToInput = false
        } else {
            okToInput = true
        }
    }
}

// function text(okToInput){
//     if(okToInput){
//         console.log('yes')
//     }
//     if(!okToInput){
//         console.log('no')
//     }
// }

function fillSquare(okToInput) {
    keyBoard.forEach(letter => {
        letter.addEventListener("click", () => {
            
        })
    })
}

function guessWord(){
    window.addEventListener("keypress", (event) => {
        if(guess.length < 5){
            guess.push(event.key)
        }

        //check answer
        if(guess[0] == answer[0] && 
            guess[1] == answer[1] &&
            guess[2] == answer[2] && 
            guess[3] == answer[3] && 
            guess[4] == answer[4] && 
            guess[5] == answer[5]){
                winning = true
            } else {
                winning = false
                userGuess 
                console.log()
            }
    })
}

guessWord()
