console.log(_.map([1, 2, 3, 4], raiseByPower(10)))

function raiseByPower (e) {
    return function (base) {
        return base ** e
    }
}