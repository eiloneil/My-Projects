var XLSX = require('xlsx')
var wb = XLSX.readFile('usersDB.xlsx')

let worksheet = {}
console.log(wb.Sheets['DB'])

worksheet['DB'] = XLSX.utils.sheet_to_json(wb.Sheets['DB'])
var db = (worksheet['DB'])
console.log(db)

for (var row of db) {
    console.log(row)
}

function signIn() {
    
    console.log('Hello')
    var inputEmail = document.getElementById('email-input').value
    var inputPassword = document.getElementById('pw-input').value

    console.log(inputEmail)
    console.log(inputPassword)

}

