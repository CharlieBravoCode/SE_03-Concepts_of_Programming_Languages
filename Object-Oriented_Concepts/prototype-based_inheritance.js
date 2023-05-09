// Run via:
// node Object-Oriented_Concepts/prototype-based_inheritance.js


const parent = {
  greet: function() {
    console.log("Hello from Parent object");
  }
};

const child = Object.create(parent);
child.greet();


// Output:
// Hello from Parent object

