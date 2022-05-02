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
console.log(person.getID());
console.log(eilon.getID());

var arr = [1, 10, 'apple']
arr.length = 100