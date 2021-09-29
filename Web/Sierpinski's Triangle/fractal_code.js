// Create Canvas
var cnv = document.getElementById('myCanvas');
var ctx = cnv.getContext('2d')
var cnvWidth = cnv.width
var cnvHeight = cnv.height
var canvasOffsetX = 7
var canvasOffsetY = 27

var CheckBox = true;
var firstIteration = true; 

var nextCoords = [0, 0];
var rnd;
var anchors;
var nextAnchor;

var anchorCoordinates = {};
var anchorColors = {};

var numIterations;

// Set Anchors' properties
// Example for triangle
var triangleAnchors = {anchor0: [cnvWidth*0.5, cnvHeight*0.05]
    ,  anchor1:  [cnvWidth*0.05, cnvHeight*0.95]
    ,  anchor2: [cnvWidth*0.95, cnvHeight*0.95]
};
var triangleColors = {anchor0: 'red'
, anchor1: 'blue'
, anchor2: 'green'
};



// Create Anchors
// drawAnchors()

var anchorsNum = Object.keys(anchorCoordinates).length
anchors = Object.keys(anchorCoordinates);

cnv.addEventListener('mousedown', function(e) {
    // alert([e.clientX, e.clientY])
    var mouseCoords = [e.clientX - canvasOffsetX, e.clientY - canvasOffsetY]
    drawCircle(ctx, mouseCoords, 15, 'black')
    var newAnchorName = 'anchor' + anchorsNum
    anchorCoordinates[newAnchorName] = mouseCoords
    anchorColors[newAnchorName] = generateColorHex()
    anchors.push(newAnchorName)
    console.log('---    Anchors Array   ---')
    console.log(anchors)
    console.log('--------------------------')
    anchorsNum ++
}, false);



function main() {
    // Starting Point
    if (firstIteration) {
        nextCoords = drawStartingPoing();
    };
    console.log("anchorCoordinates: " + anchorCoordinates);
    
    // Set number of iterations
    numIterations = parseFloat(document.getElementById('numIterations').value)
    if (!(numIterations > 0)) {
        numIterations = 100000    
    }
    console.log("Number of iterations: " + numIterations)
    
    for (var i = 0; i < numIterations; i++) {
        // sleepFor(5);
        drawNextDot();
    };

    firstIteration = false;
};

function drawNextDot() {
    rnd = getRndInteger(0, anchorsNum);
    nextAnchor = anchors[rnd];
    nextCoords = getHalfWay(nextCoords, anchorCoordinates[nextAnchor]);
    drawCircle(ctx, nextCoords, 1, anchorColors[nextAnchor]);
    
}

function presetTriangle() {
    anchorCoordinates = _.clone(triangleAnchors);
    anchorColors = triangleColors;
    anchorsNum = 3;
    anchors = Object.keys(anchorCoordinates);
    console.log(anchorCoordinates);
    drawAnchors(anchorCoordinates);
};

function drawAnchors(anchors=anchorCoordinates){
    for (var key in anchors){
        drawCircle(ctx, anchors[key], 15, fillstyle='black');
    };
};

function drawStartingPoing() {
    var startingCoords = [getRndInteger(10, cnvWidth), getRndInteger(10, cnvHeight)]
    if (CheckBox) {
        drawCircle(ctx, startingCoords, 5, 'yellow', true)
    };
    return startingCoords
}

function switchCheckbox() {
    if (CheckBox) {
        CheckBox = false
    }

    else {
        CheckBox = true
    }
}

function getHalfWay(currentCoords, nextCoords) {
    
    return [(currentCoords[0] + nextCoords[0]) / 2, (currentCoords[1] + nextCoords[1]) / 2] 
}

function drawCircle(ctx, coords, rad=10, fillstyle='red', stk=false, startAngle=0, endAngle=(Math.PI * 2)) {
    ctx.beginPath();
    ctx.arc(coords[0], coords[1], rad, startAngle, endAngle);
    
    if (stk) {
        ctx.stroke()
    }

    ctx.fillStyle = fillstyle
    ctx.fill()
}

function clearIterations(){
    clearCanvas();
    drawAnchors();
}

function clearCanvas(clearAnchors=false) {
    ctx.clearRect(0, 0, cnv.width, cnv.height);
    if (clearAnchors) {
        anchorCoordinates = {};
        anchorColors = {};
        anchors = [];
        anchorsNum = 0;
    };
    firstIteration = true;
};  

function generateColorHex() {
    return '#' + Math.floor(Math.random()*16777215).toString(16);
};

function getRndInteger(min, max) {
        return Math.floor(Math.random() * (max - min) ) + min;
      };

function sleepFor(sleepDuration){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){ 
        /* Do nothing */ 
    };
};