// reverse array of char 

// using functional method
 function reverseArray(char) {
     return char.reverse();
 } 
 inp1 = ["h","e","l","l","o"];
 console.log(reverseArray(inp1));


 // using arrow function ES6

 let rever = char => {return char.reverse()};
 console.log(rever(["h","e","l","l","o"]));