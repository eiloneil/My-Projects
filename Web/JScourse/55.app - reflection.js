var person = {
    firstName : 'default',
    lastName  : 'default',
    age : 999,
    getID : function() {
        return `My name is ${this.firstName} ${this.lastName} and I'm ${this.age} years old`
    }
};

var eilon = {
    firstName : 'Eilon',
    lastName  : 'Eilstein'
};


eilon.__proto__ = person

// Demostrate Reflection - hasOwnProperty
for (var prop in eilon) {
    console.log(`${prop} : ${eilon[prop]}`)
    if (eilon.hasOwnProperty(prop)) {
        console.log(prop + ' belongs to eilon')
    }
    else {
        console.log(prop + ' doesn\'t belong to eilon')
    }
    console.log('--------------------------')
}


// Demostrate extend - using Underscore
var Sherlock = {
    address : '24 Baker St.',
    profession : 'Private detective'
}

Sherlock.__proto__ = eilon

var Watson = {
    age : '25',
    degree : 'Doctor'
}

// EXTEND HERE
_.extend(Sherlock, Watson) // bestow Watson's properties and methods to Sherlock
for (var prop in Sherlock) {
    console.log(`${prop} : ${Sherlock[prop]}`)
    if (Sherlock.hasOwnProperty(prop)) {
        console.log(prop + ' belongs to Sherlock')
    }
    else {
        console.log(prop + ' doesn\'t belong to Sherlock')
    }
    console.log('--------------------------')
}


keys = Object.keys(Sherlock)
console.log(keys)