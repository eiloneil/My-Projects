
/*

Function Statement Vs Function Expression

*/

// Examplify hoisting
log('hello', 'bye', 'adios')

// Examplify Funciton STATEMENT
    // Stated but not invoked
function log(a='default', ...other) {
    for (var item of [a, other, arguments]) {
        if (typeof item === 'object') {
        for (var mini_item of item) {
            console.log(mini_item)
            }
        }
        else {
            console.log(item)
        }
    }
}

// Invocation happens here
// log('hello', 'bye', 'adios')



// VS

// Examplify incapability of hoisting
// func('hello', 'bye', 'adios')

// Examplify Funciton EXPRESSION
    // Created on the fly but cannot be Hoisted
var func = function(a='default', ...other) {
    for (var item of [a, other, arguments]) {
        if (typeof item === 'object') {
        for (var mini_item of item) {
            console.log(mini_item)
            }
        }
        else {
            console.log(item)
        }
    }
}

// Invocation happens here
func('hello', 'bye', 'adios')

// ---------------------------------
// IIFE - Immediately Invoked Function Expression

// Examplify IMMEDIATE INVOCATION
    // Function Expression BUT it is invoked at the end of the assignment
var func = function(a='default', ...other) {
    for (var item of [a, other, arguments]) {
        if (typeof item === 'object') {
        for (var mini_item of item) {
            console.log(mini_item)
            }
        }
        else {
            console.log(item)
        }
    }

    console.log("I've been immediately invoked!")

}();


(function(name) {
    console.log(name + ' inside an IIFE')
}('Eilon')); // Stand Alone IIFE