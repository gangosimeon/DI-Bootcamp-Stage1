
// 🌟 Exercise 1: Simple If/Else Statement
// Instructions
// Create 2 variables, x and y. Each of them should have a different numeric value.
let x = 5;
let y = 2;
// Write an if/else statement that checks which number is bigger.
if (x>y) {
  console.log(`${x} is the biggest number`);
} else {
  console.log(`${y} is the biggest number`);
}

// You should display:
// x is the biggest number


// 🌟 Exercise 2: Chihuahua
// Instructions
// Create a variable called newDog where it’s value is “Chihuahua”.
let newDog= "Chihuahua";
// Check and display how many letters are in newDog.
console.log(newDog.length);
// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
console.log(`uppercase ${newDog.toUpperCase()} and lowercase ${newDog.toLowerCase()}`);
// Check if the variable newDog is equal to “Chihuahua”
if (newDog==="Chihuahua")

// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
{
  console.log("I love Chihuahuas, it’s my favorite dog breed");
}
// else, console.log ‘I dont care, I prefer cats’
else{
  console.log("I dont care, I prefer cats ");
}

// 🌟 Exercise 3: Even Or Odd
// Instructions
// Prompt the user for a number and save it to a variable.
let nb= prompt("Enter a number ");
// Check whether the variable is even or odd.
if (Number(nb)%2===0) 
// If it is even, display: “x is an even number”. Where x is the actual number the user chose.
{
  alert(`${nb} is an even number`);
}
// If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.
else {
  alert(`${nb} is an odd number`);
}

// 🌟 Exercise 4: Group Chat
// Instructions
// Below is an array of users that are online in a group chat.

const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
// Using the array above, console.log the number of users that are connected to the group chat based on the following rules:
console.log(`There are ${users.length} users`);
// If there is no users (the users array is empty), console.log “no one is online”.
if (users.length===0) {
  console.log("No one is online");
} 
// If there is 1 user, console.log “<name_user> is online”.
else if(users.length===1) {
  console.log(`${users[0]} is online`);
}
// If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
else if(users.length===0) {
  console.log(`${users[0]} nd ${users[1]} are online`);
}
// If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
else if(users.length>2) {
  console.log(`${users[0]}, ${users[2]} and ${users.length-2} more are online`);
}
// For example, if there are 5 users, it should display:
// name_user1, name_user2 and 3 more are online
