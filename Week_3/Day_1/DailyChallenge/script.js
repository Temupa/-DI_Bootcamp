// Exercise 1:

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
console.log(fruits);
console.log(fruits.sort());
fruits.push("Kiwi");
console.log(fruits);
fruits = fruits.slice(1);
console.log(fruits);
fruits.reverse();
console.log(fruits);

// Exercise 2:

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0]);