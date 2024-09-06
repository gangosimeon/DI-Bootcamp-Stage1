// // Exercise 1 : The World Translator
// // Instructions
// // Hint: Use Switch Case

// // Ask the user which language they speak.

// let language = prompt("Entrer la langue aue vous parlez ")

// // Convert the user’s answer to lowercase, so that all the user’s inputs will be accepted in the if statement. For example “english” or “English” or “ENGlish” ect…”

// // Create a few conditions :
// switch (language.toLowerCase()) {
// // If the user speaks French : display “Bonjour”
// case "french":
//   alert("Bonjour");
//   break;

// // If the user speaks English : display “Hello”
// case "english":
//   alert("Hello");
//   break;
// // If the user speaks Hebrew : display “Shalom”
// case "hebrew":
//   alert("Shalom");
//   break;
// // If the user doesn’t speak any of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’
// default:
//   alert("01110011 01101111 01110010 01110010 01111001");
//   break;

// }
// // Exercise 2 : The Grade Assigner
// // Instructions
// // Ask the user for their grade.
// let grade = prompt("Enter your grade ");
// // If the grade is bigger than 90, console.log “A”
// let grad= Number(grade);
//  console.log(grad > 90);
// // console.log(typeof(grad));
// if (grad > 90) {
//   console.log("A")
// } 
// // If the grade is between 80 and 90 (included), console.log “B”
// else if(grad>80 && grad<=90){
//   console.log("B")
// }
// // If the grade is between 70(included) and 80 (included), console.log “C”
// else if(grad>=70 && grad<=80){
//   console.log("C")
// }
// // If the grade is lower than 70, console.log “D”
// else if(grad<70){
//   console.log("D")
// }else{
//   console.log("Enter a number!")
// }

// Exercise 3 : Verbing
// Instructions
// Prompt the user for a string. It must be a verb.
let verb = prompt("Enter a verb ");
// If the length of the string is at least 3 and the string doesn’t end with “ing”, add “ing” to the end of the string.
if (verb.length>=3 && verb[verb.length-3]+verb[verb.length-2]+verb[verb.length-1]!="ing") {
  console.log(`${verb}ing`)
} 
// If the length of the string is at least 3 and the string ends with “ing” add “ly” to it’s end.
else if (verb.length>=3 && verb[verb.length-3]+verb[verb.length-2]+verb[verb.length-1]==="ing") {
  console.log(`${verb}ly`)
} 
// If the length of the string is less than 3, leave it unchanged.
else{
  console.log(verb)
} 
// Example:

//   The string is : "read" , your program should console.log : "reading"
//   The string is : "swimming", your program should console.log : "swimmingly"
//   The string is : "go" your program should console.log : "go"