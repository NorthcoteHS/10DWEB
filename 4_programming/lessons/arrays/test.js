// Initialise Mocha/Chai.
mocha.setup('bdd');
mocha.traceIgnores = ['mocha.min.js', 'chai.min.js'];
var expect = chai.expect;
var sandbox = chai.spy.sandbox();

describe('functions', function() {
  function r(lower, upper, digits) {
    var range = upper - lower;
    var mag = Math.pow(10, digits || 0);
    var temp = Math.random() * range + lower;
    return Math.floor(temp * mag) / mag;
  }

  function s(nChars) {
    nChars = nChars || r(1,6);
    for (var i=0, out=''; i<nChars; i++) {
      var code = r(0,2) ? r(65,91) : r(97,123);
      out += String.fromCharCode(code);
    }
    return out;
  }

  beforeEach(function() {
    sandbox.on(window, 'alert', () => 0);
    sandbox.on(console, 'log', () => 0);
  });

  afterEach(function() {
    sandbox.restore();
  });

  /*
    - Create the following array: `roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah'];`
    - Log the array (using `console.log()`).
    - Students take turns each week cleaning the class guinea pig cage. Alert (using `alert()`) the name of the third student on the roll, so they know it's their turn.
    - Log the length of the array.
    - Then, add `'James'` to the end of the roll, and log the new roll.
    - `'Jordan'` changed schools. Remove him, and log the new roll.
    - `'Michael'` prefers to go by 'Mike'. Change his name, and log the new roll.
    - (Challenge) Alphabetise the roll and log.
    - (Challenge) Reverse the array and log.
    - (Challenge) Log the name of a random student in the class (not tested).
    - (Challenge) Split the array into two, each with 5 students (one with the first half of the class, the other with the second), and log like `console.log(list1, list2)`.
    */
  describe('#classRoll()', function() {
    before(function() {
      classRoll();
    });
    var roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah'];
    it('should log the initial array', function() {
      expect(console.log).on.nth(1).be.called.with(roll);
    });
    it('should alert the third child', function() {
      expect(alert).on.nth(1).be.called.with('Jordan');
    });
    it('should log the length of the array', function() {
      expect(console.log).on.nth(2).be.called.with(10);
    });
    it('should log the roll with the new student', function() {
      roll.push('James');
      expect(console.log).on.nth(3).be.called.with(roll);
    });
    it('should log the roll with Jordan removed', function() {
      roll.splice(3,1);
      expect(console.log).on.nth(4).be.called.with(roll);
    });
    it('should change Michael''s name to Mike', function() {
      roll[4] = 'Mike';
      expect(console.log).on.nth(5).be.called.with(roll);
    });
  });

});

// Run the tests.
mocha.run();
