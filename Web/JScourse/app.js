var obj1 = {a:10, b:20, c:30}
var obj2 = {a:20, b:40, c:60}

obj1 = _.clone(obj2)
obj1.a = 999


// replace()

console.log(obj2.a)