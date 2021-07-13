var eilonObj = {
    fname : 'Eilon',
    lname : 'Eilstein',
    age : 22,
    logFunc : function(){
        fullName = this.fname + ' ' + this.lname;
        return fullName;
    }

};

var getLogFunc = function(param1, param2) {
    console.log('Starting now, ' + param1 + ' ' + param2)
    console.log(this.logFunc() + " is logged")
}

getLogFunc.bind(eilonObj)('3 2', '1 GO')
getLogFunc.call(eilonObj, '3 2', ' 1 GO AGAIN')