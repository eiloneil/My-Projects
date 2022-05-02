// Map y-value for each x-value using a passed-on function argument
function x2y(arr, func) {
    var newArr = []
    for (var i=0; i < arr.length; i++) {
        newArr.push(func(arr[i]))
    }
    return newArr
}

arr = [0, 1, 2, 3, 4, 5]
console.log(arr)

function parabolla(x) {
    return x ** 2
}

function hyperbolla(x) {
    return x ** 3
}

function filter(limiter, x) {
    return x > limiter
}

function limiterFunc(limiter) {
    return filter.bind(this, limiter)
}

console.log(x2y(arr, parabolla))
console.log(x2y(arr, hyperbolla))
console.log(x2y(arr, limiterFunc(2)))