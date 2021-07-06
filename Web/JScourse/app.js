var a = 'eilon'

var i = 0

function b() {
while (i < 30) {
    console.log(i)
    i ++
    } 
}

function log(a='default', ...other) {
    console.log(a)
    console.log(other)
    console.log(arguments)
}

log('hello', 'bye', 'adios')