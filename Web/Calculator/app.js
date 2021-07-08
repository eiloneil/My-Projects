

var CurrentNum = 0;
var PreviousNum = 0;
var CurrentOp = '';
var numOfOperands = 0;
var wasCalculated = 0;
var results = 0;
var DoneCalculated = 0;

var outputElement = document.getElementById('output-id');
outputElement.innerHTML = '0';
var outputText = outputElement.innerHTML;

var preOutputElement = document.getElementById('pre-output');
var preOutputText = preOutputElement.innerHTML = 0;

var operandElement = document.getElementById('output-op');


console.log(document.getElementById('5btn'))


window.addEventListener('keyup', keyBoardPress);

function keyBoardPress(key) {
    
    var btnName = key.key;
    console.log(btnName)
    
    if (key.key === 'Enter' || key.key === 'Backspace' ) {
        btnName = operandsObj['special operands'][key.key];
        document.getElementById(btnName+'btn').onclick();
    }
    else {
        btnName = key.key
        document.getElementById(key.key+'btn').onclick();
    };
}


var operandsObj = {
    '+': function(a, b)   {
        return a + b;
    },

    '-': function(a, b)   {
        return a - b;
    },

    '/': function(a, b)   {
        return a / b;
    },

    '*': function(a, b)   {
        return a * b;
    },
    
    '': function(a, b)   {
        return a + b;
    },
    'special operands': {
        'Enter': '=',
        'Backspace': 'DEL'
    }
} 


function calcFunc(args) {
    var val = args[0];
    var stype = args[1];

    if (stype === 'num') {
        addNum(val);
    }
    else if (stype === 'op') {
        addOperand(val);
        DoneCalculated = 0;
    }
    else if (stype === 'equal'){
        numOfOperands = 0;
        Calculate();
        DoneCalculated = 1;
    }
    else if (stype === 'DEL'){
        CurrentNum = String(CurrentNum).slice(0,-1)
    }
    else if (stype === 'AC'){
        CurrentNum = '0'
        PreviousNum = 0
        CurrentOp = ''
    };
    outputText = CurrentNum
    preOutputText = PreviousNum
    outputElement.innerHTML = outputText;
    preOutputElement.innerHTML = preOutputText
    operandElement.innerHTML = CurrentOp
};


function addNum(num) {
    if (outputText === '0' || DoneCalculated == 1) {
        CurrentNum = num;
        DoneCalculated = 0;
        }
    else {
        CurrentNum += num;
    }
};


function addOperand(oprnd) {
    
    CurrentOp = oprnd;
    
    if (numOfOperands==0) {
        PreviousNum = CurrentNum;
        CurrentNum = 0;
        numOfOperands += 1;
    }
    else {
        Calculate()
        PreviousNum = results;
        CurrentNum = 0;

    }

};


function Calculate() {

    a = parseFloat(PreviousNum)
    b = parseFloat(CurrentNum) 
    console.log( typeof a)
    console.log(CurrentOp)
    results = operandsObj[CurrentOp](a, b)
    console.log('all is equal ' + results)    
    console.log(a + CurrentOp + b + ' equals ' + results)    
    CurrentNum = results
    
}
