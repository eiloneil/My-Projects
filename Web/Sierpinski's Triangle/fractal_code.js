// Create Canvas
var cnv = document.getElementById('myCanvas');
var ctx = cnv.getContext('2d')
var cnvWidth = cnv.width
var cnvHeight = cnv.height
var canvasOffsetX = 7
var canvasOffsetY = 27

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

cnv.addEventListener('mousedown', function(e) {
    // alert([e.clientX, e.clientY])
    var mouseCoords = [e.clientX - canvasOffsetX, e.clientY - canvasOffsetY]
    drawCircle(ctx, mouseCoords, 15, 'black')
    anchorCoordinates['anchor' + anchorsNum] = mouseCoords
    anchorColors['anchor' + anchorsNum] = generateColorHex()
    anchorsNum ++
}, false);



function main() {
    // Starting Point
    var nextCoords = drawStartingPoing();
    console.log(anchorCoordinates)
    
    // Set number of iterations
    numIterations = parseFloat(document.getElementById('numIterations').value)
    console.log(numIterations)
    
    var anchors = Object.keys(anchorCoordinates);
    var nextAnchor;
    var rnd;
    var rndResults = {0:0, 1:0, 2:0, 3:0, 4:0};
    for (var i = 0; i < numIterations; i++) {
        // sleepFor(5);
        rnd = getRndInteger(0, anchorsNum);
        nextAnchor = anchors[rnd];
        nextCoords = getHalfWay(nextCoords, anchorCoordinates[nextAnchor]);
        drawCircle(ctx, nextCoords, 1, anchorColors[nextAnchor]);
        rndResults[rnd] ++;
    };
};

function presetTriangle() {
    anchorCoordinates = _.clone(triangleAnchors);
    anchorColors = triangleColors;
    anchorsNum = 3;
    console.log(anchorCoordinates);
    drawAnchors(anchorCoordinates);
};

function drawAnchors(anchors=anchorCoordinates){
    for (var key in anchors){
        drawCircle(ctx, anchors[key], 15, fillstyle='black');
    };
};

function drawStartingPoing() {
    var startingCoords = [getRndInteger(10, 700), getRndInteger(10, 400)]
    drawCircle(ctx, startingCoords, 5, 'yellow', true)
    return startingCoords
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
        anchorsNum = 0;
    };
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