

const parent = {
  greet: function() {
    console.log("Hello from Parent object");
  }
};

const child = Object.create(parent);
child.greet();


// Output:
// Hello from Parent object
