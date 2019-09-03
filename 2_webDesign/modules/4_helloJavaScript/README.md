# helloJavaScript

As a recap from the CSS module, there are three main components to any "static" webpage:

1. **HTML:** The skeleton of your code, where you define your content, but *not* how it looks or behaves. This is like dragging elements from the "Palette" in App Inventor.
2. **CSS:** The styles where you define the appearance of your elements, much like changing the properties in the App Inventor "Designer".
3. **JavaScript:** The behaviour of your code. This is like the "Blocks Editor" in App Inventor.

In this task, you are going to begin learning how to program **behaviour** for your webpages using **JavaScript**.

## Steps

1. Before attempting this task, you should first complete [helloWorld](../1_helloWorld/), [helloHtml](../2_helloHtml/), and [helloCss](../3_helloCss/).

2. Create a new file and save it as `helloJavaScript.html`.

    - In the file, create the basic HTML structure, with `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`.
    - Do **not** use a template file for this task - we want you to practise the HTML structure!

3. Inside the body, make a new `<script>` tag:

    ```html
    <body>
        <script>
        </script>
    </body>
    ```
    - the `<script>` should always be the **last** element in your body, just before the `</body>` statement.

4. We are going to look at three ways to say "Hello" with JavaScript. The first is with a command called `alert()` - copy this code, then save and refresh to see what happens:

    ```html
    <script>
        alert('Hello, world!');
    </script>
    ```
    - notice that all of our JavaScript code goes inside the `<script>` element!

5. Before we look at the second method, let's take a moment to talk about "comments".
    - Normally, every line of code in your `<script>` is read by your computer and executed as an instruction.
    - Sometimes we want the computer to ignore a line of code - usually so that we can write a human-readable note about what the code is doing.
    - We call these "comments". We tell the computer to ignore a line of JS code by starting the line with `//`, or by surrounding a chunk of code (even multiple lines) with `/*` and `*/`.
    - Now, copy this comment into your code:
    ```html
    <script>
        // Method 1: Alert.
        alert('Hello, world!');
    </script>
    ```
    - Notice the comment goes before the code it refers to.

6. **Method 2:** `alert()` is easy but popups can be annoying. If we want a "quiet" message that only developers will see, we can use `console.log()`. Try it:

    ```html
    <script>
        // Method 2: Console.log.
        console.log('Hello, world!');
    </script>
    ```
    - Notice we have deleted Method 1 for now.
    - Also notice, when you save and refresh, nothing is displayed!
    - We need to look at the "console", a very useful web programming tool. To open it, in your browser (Chrome/Firefox/IE/Safari):
        - Press F12 (may need to use the "Function" key), or Right Click anywhere on a page and select "Inspect", to open the "Inspector"
        - Find a tab that says Console and click on it (differs between browsers)
    - In the console you should see our message, "Hello, world!"

7. **Method 3:** Alert is annoying and `console.log` is only for developers looking at the console. To properly communicate with users, we want to display a message in the *body* of the webpage.

    - First, create an empty `<p>` element in your body, with an ID of "target".
    - Then use the JavaScript command `document.getElementById("target")` to get a *pointer* to that `<p>` element, based on its ID.
    - Finally, we can change the `<p>` element's text by setting its `.innerHTML` property to `'Hello, World!'`
    - Putting that all together:
    ```html
    <body>
        <p id="target"></p>
        <script>
            // Method 3: getElementById and innerHTML.
            document.getElementById('target').innerHTML = 'Hello, World!';
        </script>
    </body>
    ```
    - Notice, this is the *hardest* of the three methods, but it gives the nicest result.

### Next step: Logic

We have looked at three different ways to display text to the user. Next is a brief introduction to *logic* - that is, having the computer make decisions.

1. Earlier we looked at each display method individually. Now, put all three back into your code:
    ```html
    <script>
        // Method 1: Alert.
        alert('Hello, world!');
        // Method 2: Console.log.
        console.log('Hello, world!');
        // Method 3: getElementById and innerHTML.
        document.getElementById('target').innerHTML = 'Hello, World!';
    </script>
    ```
    - If we leave it like that, all three methods will run, one after another.
    - That's not good - we want it to do only one (but we want to be able to pick which one!)

2. At the heart of all programming is the idea of **variables**. These are differnet from maths variables - in programming, a variable is a named object in which we can store information.

    - In JavaScript we *create* a variable with the `var` keyword, and *set* it to a value using `=`.
    - Create a variable in your script called `method` with the value `"console"`:
    ```html
    <script>
        var method = "console";
        // Method 1: Alert.
        ...
    </script>
    ```

3. Another central concept in programming is the **if statement**. It tells a computer to run a piece of code *if (and only if)* some condition is true.

    - We can now create if statements to run the method we've chosen with `method`:
    ```html
    <script>
        var method = "console";
        // Method 1: Alert.
        if (method == "alert") {
            alert('Hello, world!');
        }
        // Method 2: Console.log.
        if (method == "console") {
            console.log('Hello, world!');
        }
        // Method 3: getElementById and innerHTML.
        if (method == "innerHTML") {
            document.getElementById('target').innerHTML = 'Hello, World!';
        }
    </script>
    ```
    - Notice the "syntax" for if statements - that is, the specific format they must take:
    ```js
        if (someCondition) {
            someAction();
        }
    ```

4. That's it! You can now change the value of `method` in your code between `"alert"`, `"console"`, and `"innerHTML"`, and it should use your chosen method.

## Extension

There are three main extension tasks for this assignment:

1. Research [else and else if](https://www.w3schools.com/js/js_if_else.asp), and change our three `if` statements using your new knowledge.

2. Right now our code runs as soon as the webpage loads. Instead, make it say hello when a **button** is clicked.

    - Research [JavaScript functions](https://www.w3schools.com/js/js_functions.asp) and the button [onclick event](https://www.w3schools.com/jsref/event_onclick.asp).
    - In your `<script>`, move *all* of our previous code into a function called `action()`.
    - Create an HTML button (in the body) with an onclick attribute that calls `action()`.

3. When we wrote `var method = "console";` we did something known as "hard-coding" - we put the value of `method` directly into our code, rather than letting the user choose it.

    - Before doing this extension, you must have completed Extension 2 (creating a button for the event).
    - Create an [`<input type="text">`](https://www.w3schools.com/tags/att_input_type.asp) object in your HTML body.
    - Put instructions in your HTML body for the user to type "alert", "console", or "innerHTML" into the text box, then click your button.
    - Research the [input text value property](https://www.w3schools.com/jsref/prop_text_value.asp) to find out how to get the value they have typed *inside* your function that is called when the button is clicked.
    - Use that value instead of our pre-programmed value of `method` to run your if statements.

## Next steps

Congratulations! This was a very brief introduction to the large world of programming in JavaScript.

When you're finished this module, please head on over to Codecademy and begin the [Introduction to JavaScript course](https://www.codecademy.com/learn/introduction-to-javascript). Enjoy!
