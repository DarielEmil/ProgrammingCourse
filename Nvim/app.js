console.log('Hola')
//document.write('<h1>Hello World, Javascript</h1>')

//console.error('Mi error custimizado')

//!DataType

//"Hello World" o 'Hello World' //* String

//* Number
//1 2 3 4  
//-2.3
//10.5

//* Boolean
//true  
//false

//! Array
//['Joe', 'Ryan', 'Martha']
//[1, 2, 3]
//[true, false, true, false]

//! Object

//{
  //"username": 'Ryan',
  //"score" : 70.4,
  //"Hours" : 14
  //"proffesional" : true
//}

//console.log({
  //'Username': 'Bryan',
  //'LastName': 'Garcia',
  //'Score' : 5,
  //'Age' : 20 
//});

//! Variable Types

// var Data = {
//   "UserName": "John",
//   "Country": "USA"
// }

var Name = 'John'; //* Variable
let name = 'Carla'; //* Variable

const PI = 3.1415; //* Constante

// console.log(PI)

//! Operadores

//TODO Suma = +
//TODO Resta = - 
//TODO Multiplicacion = *
//TODO Division = /

var NumberOne = 10;
var NumberTwo = 10;

var Result = NumberOne + NumberTwo;

// console.log(Result)

let Nombre = 'Carlos';
let LastName = 'Garcia';

let completeName = Nombre + LastName //! Concatenacion

// console.log(completeName)

//! Conditional Operators

let numberOne = 10;
let numberTwo = 100;

let Boolean = numberOne <= numberTwo;

console.log(Boolean)

//! Conditional 

// if (numberOne == numberTwo){
//   console.log('Es falso')
// } else if (numberOne < numberTwo){
//   console.log('Es verdadero')
// } else{
//   console.log("Hola")
// }


//! Other Conditional 

switch(numberOne){
  case 10:
    console.log('Es menor')
    break
  case numberOne >= 1:
    console.log('Es mayor')
  default:
    console.log('Ninguna de las anteriores')
}

//! Loop while

// while(numberOne != 20){
//   console.log('Hello world');
//   console.log(numberOne);
//   numberOne++;
// };

//! Loop For

// for (let x = 0; x < 10; x++ ){
//   console.log(x)
// }


//! Length

// Box = ['a','e','i','u','o']

// console.log(Box.length);

//! Function

function Greeting(Args){
  console.log(Args)
}

Greeting('World');

console.table()
