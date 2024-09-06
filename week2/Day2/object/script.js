// Exercise 1
// Create a stuctured html file linked to a JS file

// 1. Create an object that has properties "username" and "password". Fill those values in with strings.
let count={
  username: "gango",
  password:"1234@"
};
console.log(count);
// 2. Create an array which contains the object you have made above and name the array "database".
let database = [count];
console.log(database);
// 3. Create an array called "newsfeed" which contains 3 objects with properties "username" and "timeline".
let newsfeed =Array(
  {
    username:"zongo",
    timeline:"12/9/2024"
  },
  {
    username:"pierre",
    timeline:"6/9/2024"
  },
  {
    username:"ouedraogo",
    timeline:"10/9/2024"
  }
);

console.log(newsfeed);