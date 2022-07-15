### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python and JS are very simliar, typically Python is used for backend while JS is for front end. I would argue that the Python syntax is easier to read than JS. Python is also much more complex than JS considering it has so many different libraries and build in modules to create complex backend of web pages and software. JS is more dynamic client side and can really make a page pop and impressive through thte differetn features it offers with events listeners. Both can be used for front end or back end but belong respectively in their place.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  number.setdefault('c', 3)

- What is a unit test?
A unit test is a test done on one componenet of the entire codebase. For example a python code full of algorithms a unit test could be done on each algorithm.

- What is an integration test?
An integration test is a test to see how all of the different components of an application run in unicent.

- What is the role of web application framework, like Flask?
Flask gives the opportunity to have multiple web pages to be linked together. Also can get information from HTML it is linked to.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  It would depend on what it is needed for. Will a page specifically on pretzels and the history and background of pretzels need to be opened? Then i would opt for '/foods/pretzel'. If it is an option in a 'favorite food' list then I would choose 'foods?type=pretzel'.

- How do you collect data from a URL placeholder parameter using Flask?
'/some_url/<user>'
request.args(user)
- How do you collect data from the query string using Flask?
request.args()
- How do you collect data from the body of the request using Flask?
request.form()

- What is a cookie and what kinds of things are they commonly used for?
A cookie is saved data in a session or length of time. It can be used for banners or maybe a shopping cart.

- What is the session object in Flask?
A session is the interval a person log in and then out of the server.

- What does Flask's `jsonify()` do?
'jsonify' converts arguments into a dictionary of key value pairs.
