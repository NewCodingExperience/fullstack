class Dog {
    constructor(name) {
      this._name = name;
      this._behavior = 0;
    }
  
    get name() {
      return this._name;
    }
    get behavior() {
      return this._behavior;
    }   
  
    incrementBehavior() {
      this._behavior ++;
    }
  }
  
  const halley = new Dog('Halley');
  console.log(halley.name); // Print name value to console
  console.log(halley.behavior); // Print behavior value to console
  halley.incrementBehavior(); // Add one to behavior
  console.log(halley.name); // Print name value to console
  console.log(halley.behavior); // Print behavior value to console
  
//   examples:
// Similar to Java, due to using the constructor and using the parameter and the this assign to the parameter.
// Creating objects but using consts.
class Surgeon {
    constructor(name, department) {
      this.name = name;
      this.department = department;
    }
  }
  
  const surgeonRomero= new Surgeon('Francisco Romero','Cardiovascular');
  const surgeonJackson= new Surgeon('Ruth Jackson','Orthopedics');
  