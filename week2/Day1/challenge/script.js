// Instructions
// Exercise 1:
// Using this array :

const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// Remove Banana from the array.
fruitsList= fruits.splice(0,1);
console.log(fruits);
// Sort the array in alphabetical order.
//fruits.sort();
fruits.toSorted()
console.log("frts= " +fruits);
// Add “Kiwi” to the end of the array.
fruits.push("Kiwi");
console.log(fruits);
// Remove “Apples” from the array. Don’t use the same method as in part 1.
fruits.shift('Apples');
console.log(fruits);
// Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
fruits.toSorted();
fruits.reverse();
console.log("reverse array= " + fruits);
// At the end you should see this outcome:

// ["Kiwi", "Oranges", "Blueberries"]




// Exercise 2:
// Using this array :

const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// Access and then console.log “Oranges”.
console.log(moreFruits[1][1][0])