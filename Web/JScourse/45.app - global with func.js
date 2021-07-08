// IIFE
(
    function(greet) {
        var greeting = greet

        // so far, the window.greeting var in the global scope is "Hola"
        this.greeting = window.greeting
        
        // Now we've intentionally mutated the greeting Property of the object window
        console.log(this)
    }
)('Hello')

// console.log(greeting)