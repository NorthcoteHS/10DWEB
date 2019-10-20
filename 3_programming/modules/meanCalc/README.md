# meanCalc

Your task is to create a program that gets numbers from the user, and calculates their average (mean).

## Steps

1. Always start by opening Brackets, creating a new file, and saving it.

    - Save the new file as `meanCalc.html`.
    - Fill out the basic structure of the HTML from memory, or use a template or past project.

2. In JavaScript, create an empty array.

2. Get a number from the user, using either `prompt()` or an HTML `<input>` and `<button>`, and add it to the end of the array.

    - Remember to convert it into a number first (using `parseInt()` or `parseFloat()`)!

3. Repeat Step 2 until the user has entered all their desired numbers.

    - How will you know when to finish? You could have an exit condition (e.g. `Type 'quit' to finish`), or ask how many numbers before starting...
    - If using HTML inputs, you will probably want a separate button to finish.

4. Use a loop to add all numbers together, then divide the sum by `n` (the length of the array).

    - Think about how this should work!
    - Generally we create a variable and start it at 0 *before* the loop (e.g. `var sum = 0;`), then in the loop we increase it by each value in the array.

5. Display the average, using `alert()` or using HTML.

6. Use the resources below to guide you through the process.

## Resources

| Requirement | Resource |
|-------------|----------|
| Arrays               | <ul><li>[JavaScript arrays](https://www.w3schools.com/js/js_arrays.asp) (look at "Creating" and "Access the Elements")</li></ul> |
| Loops                | <ul><li>[JS while loop](https://www.w3schools.com/js/js_loop_while.asp)</li><li>[JS for loop](https://www.w3schools.com/js/js_loop_for.asp)</li><li>[Looping through each character in a string (StackOverflow)](https://stackoverflow.com/a/1967132/4080966)</li></ul> |
| Math operations      | <ul><li>[JavaScript arithmetic](https://www.w3schools.com/js/js_arithmetic.asp)</li><li>[JavaScript Math object](https://www.w3schools.com/js/js_math.asp)</li></ul> |
| General     | <ul><li>[StackOverflow](https://stackoverflow.com/)</li><li>[W3Schools](https://www.w3schools.com/)</li><li>[CSS-Tricks](https://css-tricks.com/)</li><li>[Course Resources](/resources/)</li></ul> |

For HTML versions (using `<input>`, buttons, and `.innerHTML`):

| Concept              | Resource |
|----------------------|----------|
| Input elements | <ul><li>[Different input types (W3Schools)](https://www.w3schools.com/tags/att_input_type.asp)</li></ul> |
| Buttons     | <ul><li>[HTML button element](https://www.w3schools.com/tags/tag_button.asp)</li><li>[Button onclick event (linking to functions)](https://www.w3schools.com/jsref/event_onclick.asp)</li></ul> |
| Getting HTML content | <ul><li>[getElementById() (W3Schools)](https://www.w3schools.com/jsref/met_document_getelementbyid.asp)</li><li>[Input text value property (W3Schools)](https://www.w3schools.com/jsref/prop_text_value.asp)</li><li>[Getting dropdown selection value (W3Schools)](https://www.w3schools.com/jsref/prop_select_value.asp)</li></ul> |
| Displaying results   | <ul><li>[JavaScript output summary (W3Schools)](https://www.w3schools.com/js/js_output.asp)</li><li>Option 1: [JS alert box](https://www.w3schools.com/js/js_popup.asp)</li><li>Option 2: [Changing HTML content](https://www.w3schools.com/js/js_htmldom_html.asp)</li><li>Option 3: [console.log](https://www.w3schools.com/jsref/met_console_log.asp)</li></ul> |

## Extension

- Use HTML input/output, and have the average display automatically after each number is added, along with the number of values.
- Create a weighted average program - each value has an associated weight, which increases/decreases its contribution to the average.
    - e.g. values `[10, 10, 10, 12]` with weights `[1, 1, 1, 3]` has an average of `11` (`(10+10+10+12*3) / 6 = 11`).
- Generate additional statistics, like min, max, standard deviation, etc.

## Assessment

| Level  | Expectations |
|--------|--------------|
| Bronze   | Receives a variable amount of numbers, and calculates and displays the average. |
| Silver   | Displays the average and n automatically after each value is added (via HTML). |
| Gold     | Implements one or more of the challenges. |

- **Note:** all code should be commented and you should have no redundant code.

Remember to commit each time you've made a major change to your code, and to push to GitHub frequently.
