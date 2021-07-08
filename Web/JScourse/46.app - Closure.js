function greet(whattosay) {
    return function(name) {
        console.log(whattosay + ' ' + name)
    }
}

greet('Hi there')('Eilon')


////////////////////////////////


function BuildFunc(){
    
    var arr = []
    
    for (var i = 0; i < 3; i++) {
        arr.push(
            function() {
                console.log(i)
            }
            );
        };
        
        return arr
};

arrs = BuildFunc()
console.log('Demonstrate Closure')

arrs[0]();
arrs[1]();
arrs[2]();

////////////////////////////////


function BuildFunc2(){
    
    var arr = []
    
    for (var h = 0; h < 3; h++) {
        let j = h
        arr.push(
            function() {
                console.log(j)
            }
            );
        };
        
        return arr
};

arrs2 = BuildFunc2()
console.log('Bypass Closure using Let statement')

arrs2[0]();
arrs2[1]();
arrs2[2]();



////////////////////////////////


function BuildFunc3(){
    
    var arr = []
    
    for (var h = 0; h < 3; h++) {
        arr.push(
            (function(j) {
                return function() {
                    console.log(j)
                }

            })(i)
            );
        };
        
        return arr
};

arrs2 = BuildFunc2()
console.log('Bypass Closure using IIFE')

arrs2[0]();
arrs2[1]();
arrs2[2]();