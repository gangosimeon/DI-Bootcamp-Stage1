//Exercie1

// Make a keyless car!

// This car will only let you drive if you are over 18. Make it do the following:
let x;
// Using prompt() and alert(), ask a user for their age.
let age = prompt("Votre age", x);

// IF they say they are below 18, respond with: "Sorry, you are too young to drive this car. Powering off
if (age <18) {
  alert(` Only ${age} years old ?? Sorry, you are too young to drive this car. Powering off`);
}
// IF they say they are 18, respond with: "Congratulations on your first year of driving. Enjoy the ride!
else if(age ===18){
  alert("Congratulations on your first year of driving. Enjoy the ride!");
}
// IF they say they are over 18, respond with: "Powering On. Enjoy the ride!"
else{
  alert("Powering On. Enjoy the ride!");
}


// Exercise 2
// Write as comments the steps of the resolution of this piece of code

// Guess what will be the result before checking it



let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Too small' );
    break;
  case 4:
    alert( 'Exactly!' );
     //Output : Exactly!
    break;
  case 5:
    alert( 'Too large' );
    break;
  default:
    alert( "I don't know such values" );
}


// Exercise 3
// Write as comments the steps of the resolution of this piece of code

// Guess what will be the result before checking it



let b = 2 + 2;

switch (b) {
  case 4:
    alert('Right!');
    //Output : Right!
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}