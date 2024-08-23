//Exercice 1
let favoriteFood="Rice";
let favoriteMeal="lunch";
console.log("I eat "+favoriteFood+" at every "+favoriteMeal);


//Exercice 2

//Part I

const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];


let myWatchedSeriesLength=myWatchedSeries.length;



// let myWatchedSeriesSentence= myWatchedSeries[0]+','+myWatchedSeries[1]+',and '+myWatchedSeries[2];
let myWatchedSeriesSentence=`${myWatchedSeries[0]}, ${myWatchedSeries[1]},and ${myWatchedSeries[2]}`;

console.log(`I watched ${myWatchedSeriesLength} series : ${myWatchedSeriesSentence}`);

//Part II

myWatchedSeries.splice(2,1,'friends');
console.log(myWatchedSeries);

myWatchedSeries.push('Jack Bauer');
console.log(myWatchedSeries);


myWatchedSeries.unshift('Prison Break');
console.log(myWatchedSeries);

myWatchedSeries.splice(1,1);
console.log(myWatchedSeries);


console.log(myWatchedSeries[1][2]);



console.log(myWatchedSeries);


//Exercise 3 : The Temperature Converter

let temperatureCelsius = 35;

let temperatureFahrenheit= (temperatureCelsius/5)*9+32;
console.log(`${temperatureCelsius}°C is ${temperatureFahrenheit}°F.`)



//Exercise 4 : Guess The Answers #1


let c;
let a = 34;
let b = 21;

console.log(c)

console.log(a+b) //first expression
// Prediction: It will Output 55
// Actual:55

a = 2;

console.log(a+b) //second expression
// Prediction: It will Output 23
// Actual:23


//1-the outcome of a + b in the first expression will be 55
//2-the outcome of a + b in the first expression will be 23
//3-the valur of c is undefinite


//4-the outcome of console.log(3 + 4 + '5'); will be 75



//Exercise 5 : Guess The Answers #2


//1-
typeof(15)
// Prediction:number 
// Actual:number

typeof(5.5)
// Prediction:number
// Actual:number

typeof(NaN)
// Prediction:number
// Actual:number

typeof("hello")
// Prediction:string
// Actual:string

typeof(true)
// Prediction:boolean
// Actual:boolean

typeof(1 != 2)
// Prediction:boolean
// Actual:boolean

"hamburger" + "s"
// Prediction:hamburgers
// Actual:string
"hamburgers" - "s"
// Prediction:NaN
// Actual:number

"1" + "3"
// Prediction:13
// Actual:string

"1" - "3"
// Prediction:-2
// Actual:number

"johnny" + 5
// Prediction:johnny5
// Actual:String

"johnny" - 5
// Prediction:NaN
// Actual:number

99 * "hello"
// Prediction:NaN
// Actual:number

1 != 1
// Prediction:false
// Actual:boolean

1 == "1"
// Prediction:true
// Actual:boolean

1 === "1"
// Prediction:false
// Actual:boolean


//Exercise 6 : Guess The Answers #3



5 + "34"
// Prediction:534
// Actual:String

5 - "4"
// Prediction:1
// Actual:number

10 % 5
// Prediction:0
// Actual:number

5 % 10
// Prediction:5
// Actual:number

" " + " "
// Prediction:
// Actual:string

" " + 0
// Prediction: 0
// Actual:string

true + true
// Prediction:2
// Actual:number

true + false
// Prediction:1
// Actual:number

false + true
// Prediction:1
// Actual:number

false - true
// Prediction:-1
// Actual:number

!true
// Prediction:false
// Actual:boolean

3 - 4
// Prediction:-1
// Actual:number
