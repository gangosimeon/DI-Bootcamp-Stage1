// Exercise 1 : Evaluation
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

// Evaluate the comparisons found below:

// Look at this link for help

    5 >= 1 //true;
    0 === 1//false
    4 <= 1 //false
    1 != 1//false
    "A" > "B"//false
    "B" < "C" //True
    "a" > "A" //true
    "b" < "A"//false
    true === false//false
    true != true//false


// Exercise 2 : Ask For Numbers
// Instructions
let str;
// Ask the user for a string of numbers separated by commas
let str1 = prompt('Entrer un nombre contenant une virgule',str);

// Console.log the sum of the numbers.
// Hint: use some string methods
const arrVal = str1.split(',');
const sum=Number(arrVal[0]) + Number(arrVal[1])
console.log(arrVal);
console.log(`"${arrVal}"➞ ${sum}`);
// Examples
// "2,3"➞ 5



// Exercise 3 : Find Nemo
// Instructions
// Hint: if statement (tomorrow’s lesson)
let phrase 
// Ask the user to give you a sentence containing the word “Nemo”. For example "I love the movie named Nemo"
let phrse=prompt("Entrer une phrase contenant 'Nemo'",phrase);
// Find the word “Nemo”
let list = phrse.split(' ');
let index = list.indexOf('Nemo',0);

// Console.log a string as follows: "I found Nemo at [the position of the word Nemo]".
// If you can’t find Nemo, console.log “I can’t find Nemo”.
if (index!=-1) {
    console.log("I found Nemo at "+index);
} else {
    console.log("I can’t find Nemo");
}
// Some examples:

//     "I love the movie named Nemo" ➞ "I found Nemo at 5"
//     "Nemo is a cute fish" ➞ "I found Nemo at 0"
//     "My fish is called Nemo, I love it" ➞ "I found Nemo at 4"



// Exercise 4 : Boom
// Instructions
// Hint: if statement (tomorrow’s lesson)
let nbre;
let n;
// Prompt the user for a number. Depending on the users number you will return a string of the word “Boom”. Follow the rules below:
let nb=prompt("Entrer un nombre",nbre);
// If the number given is less than 2 : return “boom”
if (Number(nb)<=2) {
    console.log('boom');
}else if (Number(nb)>2) {
    n=0;
    let mt ='o';
    //If the number given is bigger than 2 : the string should include n number of “o”s (n being the number given)
    while (n<Number(nb)-1) {
        mt=mt+'o';
        n++;
    }
    if(Number(nb)%2===0 && Number(nb)%5===0){
        // If the number given is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
        let mot=`B${mt}m`;
        console.log(mot.toUpperCase()+'!');
    }else if(Number(nb)%5===0){
        // If the number given is evenly divisible by 5, return the string in ALL CAPS.
        let mot=`B${mt}m`;
        console.log(mot.toUpperCase());
    } else if(Number(nb)%2===0){
        // If the number given is evenly divisible by 2, add a exclamation mark to the end.
        console.log(`B${mt}m !`);
    } else{
        console.log(`B${mt}m`);
    }
}


// Examples
// 4 ➞ "Boooom!"
// // There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)
// 1 ➞ "boom"
// // 1 is lower than 2, so we return "boom"

