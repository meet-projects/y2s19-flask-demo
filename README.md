# y2s19-flask-demo

## Demo 1 - Basic Flask
Open a terminal and run the webserver with the command `python example1.py`. Then open a web browser and navigate to the localhost IP address at the URL http://127.0.0.1:5000/ 
<br />
Make a change to the string being shown and save the python file. See how both the terminal and the website update.
<br />
Note how currently the website is available on localhost, but if we add the parameter `host= '0.0.0.0' ` to `app.run()`, then it will be available on the network at the computer's IP address. You can try this and have students visit the demo site from their computers.

## Demo 2 - Templates
Run `python example2.py` and notice how it now renders the "hello.html" page. Ask yourself, how is this different from just opening up "hello.html"

## Demo 3 - CSS
For CSS stylesheets, we need to put a static folder in web project folder and populate it with css documents.
Then in the html templates, we need to link the stylesheet ` <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">`
<br />
Run `python example3.py` and see how the stylesheet is applied as it was during the CSS lessons.

## Demo 4 - Variables
Show how to pass in variables into `render_template`, and note how these parameters are default aguments, so if they weren't put there, the variables would have the default value of a blank string. In the html, the variables are written in a code format similar to python, but surrounded by brackets `{{variable}}`, that way the `render_template` function will recognize it as code. What do you think will happen if you don't include the brackets?
<br />
Run `python example4.py` to see the example.


## Demo 5 - Loops
Loops in html templates are similar to python, but they need an `{% endfor %}` line at the bottom of the for loop. How in Python does the syntax show the end of a for loop? Why wouldn't that work in html?
<br />
Run `python example5.py` to see an example of loops.


## Demo 6 - Conditionals
Similar to loops, conditionals need an `{% endif %}`. Run `python example6.py` to see an example of loops.
