// Exercise 1 : Favorite Color
// Instructions
// let sentence = ["my","favorite","color","is","blue"];
// Write some simple Javascript code that will join all the items in the array above, and console.log the result.

let sentence = ["my","favorite","color","blue"];
let concat = sentence.join(" ");
console.log(concat)



// Exercise 2 : Mixup
// Instructions
// Create 2 variables. The values should be strings. For example:
// let str1 = "mix";
// let str2 = "pod";

let str1 = "mix";
let str2 = "pod";


// 2. Slice out and swap the first 2 characters of the two strings from part 1.
let st1= str1[0]+str1[1]+str2[2];
console.log(st1)
let st2= str2[0]+str2[1]+str1[2];
console.log(st2)
// 3. Create a third variable where the value is the concatenation of the two strings from the part 1 (separated by a space).
let str = str1+' '+str2;


// 4. Finally console.log the new concatenated string.
console.log(str);
console.log(`${str1} ${str2}`);


// Exercice 3 : Calculatrice
// Instructions
// Fabriquez une calculatrice. Suivez les instructions :

let n1;
let m1;
//1. Demandez à l’utilisateur le premier numéro.
let n = prompt('Entrer un nombre',n1);

//2. Stockez le premier nombre dans une variable appelée .
let num1= Number(n);
//Astuce : console.log le type de la variable . Que devez-vous faire pour le convertir en nombre ?num1num1
console.log('num1= '+num1);
console.log(typeof(num1));
//3. Demandez à l’utilisateur le deuxième numéro.
let m = prompt('Entrer un nombre',m1);
//4. Stockez le deuxième nombre dans une variable appelée .num2
let num2= Number(m);
//5. Créez une alerte dont la valeur est la SOMME de et . num1num2
alert(`num1 + num2 = ${num1+num2}`);
// BONUS : Créez un programme qui peut soustraire, multiplier et aussi diviser !
alert(`num1 - num2 = ${num1-num2}`);
alert(`num1 / num2 = ${num1/num2}`);