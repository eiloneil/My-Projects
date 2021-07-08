var a = 'eilon'

var i = 0

function b() {
while (i < 30) {
    console.log(i)
    i += 1
    } 
}

b()

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

log('hello', 'bye', 'adios');


function LoopInts(num) {
    for (var i = 0; i < num; i++) {
        console.log(i);
    };
};

LoopInts(10)