# blockStyle

Let's play with blocks!

Your task is to create a program that shows an HTML block (div), and lets the *user* change its size and colour.

## Steps

1. Before attempting this task, you should first complete [helloHtml](../2_helloHtml/) and [helloCss](../3_helloCss/).

2. Always start by opening Brackets, creating a new file, and saving it.

    - Save the new file as `blockStyle.html`.
    - Fill out the basic structure of the HTML from memory, or use a template or past project.

3. Create the HTML:

    - one `<div>` with an ID so it can be re-styled
    - optionally, several `<input>`s and a `<button>` for the user to interact with

4. Ask the user what background-color, width, and height to make the block (either using `<input>` or `prompt()`).

5. Get the user's response, and update the style of the element.

    - To interact with the element, you will need to "get" the element in JS: `document.getElementById('yourID')`
    - You can modify the element's style like so: `document.getElementById('yourID').style.width = '50px';`
    - Note that width and height always require units like `px` (pixels) or `cm` (centimetres)

6. Use the resources below to guide you through the process.

## Resources

| Concept              | Resource |
|----------------------|----------|
| Divs        | <ul><li>[Div tag (W3Schools)](https://www.w3schools.com/tags/tag_div.asp)</li></ul> |
| Manipulating CSS     | <ul><li>[JavaScript changing CSS (W3Schools)](https://www.w3schools.com/js/js_htmldom_css.asp)</li></ul> |
| Colors        | <ul><li>[CSS Colors (W3Schools)](https://www.w3schools.com/cssref/css_colors_legal.asp)</li></ul> |
| Height/Width  | <ul><li>[CSS Height and width](https://www.w3schools.com/css/css_dimension.asp)</li></ul> |
| CSS Summary   | <ul><li>[List of CSS Properties](https://www.w3schools.com/cssref/)</li></ul> |
| General     | <ul><li>[StackOverflow](https://stackoverflow.com/)</li><li>[W3Schools](https://www.w3schools.com/)</li><li>[CSS-Tricks](https://css-tricks.com/)</li><li>[Course Resources](/resources/)</li></ul> |

For HTML versions (using `<input>`, buttons, and `.innerHTML`):

| Concept              | Resource |
|----------------------|----------|
| Input elements | <ul><li>[Different input types (W3Schools)](https://www.w3schools.com/tags/att_input_type.asp)</li></ul> |
| Buttons     | <ul><li>[HTML button element](https://www.w3schools.com/tags/tag_button.asp)</li><li>[Button onclick event (linking to functions)](https://www.w3schools.com/jsref/event_onclick.asp)</li></ul> |
| Getting HTML content | <ul><li>[getElementById() (W3Schools)](https://www.w3schools.com/jsref/met_document_getelementbyid.asp)</li><li>[Input text value property (W3Schools)](https://www.w3schools.com/jsref/prop_text_value.asp)</li><li>[Getting dropdown selection value (W3Schools)](https://www.w3schools.com/jsref/prop_select_value.asp)</li></ul> |

## Extension

- Adjust more styles (see the [full list of CSS properties](https://www.w3schools.com/cssref/) for inspiration!)
- Error-proof the inputs, with dropdown lists and/or checks to make sure entered styles are valid.
- Allow the user to create multiple blocks with different styles.
- Do something else creative!

## Assessment

| Level  | Expectations |
|--------|--------------|
| Bronze | Allows user to specify width, height, and background-color. |
| Silver | Provides access to more styles and has error-proofing. |
| Gold   | All of above, plus multiple blocks! |

- **Note:** all code should be commented and you should have no redundant code.

Remember to commit each time you've made a major change to your code, and to push to GitHub frequently.
