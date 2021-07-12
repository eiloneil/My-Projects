
window.addEventListener('keyup', keyBoardPress);

function keyBoardPress(key) {
    
    var pressedKey = key.key;
    var finalVal;

    if (key.key === 'Enter' || key.key === 'Backspace' ) {
        finalVal = 'Special Value';
    }
    else {
        finalVal = key.key
    };
    console.log(finalVal)
}