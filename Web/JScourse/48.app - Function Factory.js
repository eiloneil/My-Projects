function buildFunction(age=10) {
    return function(fname='Eilon', lname='Eilstein') {
        if (age > 60) {
            console.log(fname + ' ' + lname + ", You're likely to get sick!");
        }
        else {
            console.log(fname + ' ' + lname + ", You're UNLIKELY to get sick!");
        };
        console.log("You're " + age + ' YO');
    };
};

var Old = buildFunction(80)
var Young = buildFunction(20)

Old()
console.log('')
Young()