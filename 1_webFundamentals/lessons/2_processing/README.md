# processing

To interact with a user we need input and output.
But usually, between when we're given input and when we send output, we need to make some decisions about what to do - this is called processing.

## Math operations

The most basic processing we can do are math operations like `+`, `-`, `*` (multiply), and `/` (divide).
Using these we can create new variables, or even output directly:

```js
var x = 5;
var y = x + 1;
alert(y);       // Displays 6.
alert(x+1);     // Also displays 6!
```

You can do complex math, including using brackets etc.
Some math needs to be done using the special `Math` library, like `Math.pow()`, which raises a number to a power.

```js
alert(1+5-3*2/6);   // Displays 5.
alert(1+(5-3)*2/4); // Displays 2.
alert(Math.pow(5,2));   // Displays 25. (5^2 = 25).
```
