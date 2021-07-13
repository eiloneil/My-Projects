
var txtBox = document.getElementById('txtInput')

txtBox.addEventListener('keyup', keyBoardPress);

function keyBoardPress(key) {
    
    var pressedKey = key.key;
    var finalVal;

    if (key.key === 'Enter' || key.key === 'Backspace' ) {
        finalVal = 'Special Value';
        alert('Pressed Special Key')
    }
    else {
        finalVal = key.key
    };
    console.log(finalVal)
}   