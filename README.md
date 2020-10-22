# papajohnsapi
A Python module that will allow users to use selenium to order pizza from Papa Johns.

## Disclaimer
* This only works in the United States.

* All responsibilites to use this appropriately are on the user. (It's not my fault if you put this in a `while True` loop and go 3254853478327 trillion dollars in debt.)

## Requirements
`pip install selenium`
If you are using the Chrome Browser, download the compatible version of the chromedriver [here](https://chromedriver.chromium.org/).
If you are using the Firefox Browser, download the compatible version of the geckodriver [here](https://github.com/mozilla/geckodriver/releases).
On OSX make sure to move either of these drivers to `/usr/local/bin` with either:
`mv geckodriver /usr/local/bin`
or 
`mv chromedriver /usr/local/bin`

## Installation
To Install:

`pip install papajohnsapi-mehtaarn000`

## Usage
First, import the module after downloading with:
`import papajohnsapi as pizza`

Check the menu with:
`pizza.menu(item)`
This item can be: 'Pizza', 'Drinks', 'Sides', or 'Desserts'
(Currently you can only order pizza)
Replace Arguments as needed.

Specify your choice of browser and the choice of going headless (You won't see a browser window) with:
`pizza.browser('Firefox', headless=False)`
Replace arguments as needed.

Specify your address with:
`pizza.address(house number, street, city, state, zipcode)`
Note: State must be in 2 letter form. For example, New York would be NY.
Replace arguments as needed.

Specify who you want ordering with:
`pizza.user(first name, last name, phone number, email)`
Replace arguments as needed.

Then, place your order with:
`pizza.order([items])`

Replace `items` with the order codes provided by:
`pizza.menu(item)`

Finally, kick back as you get fresh pizza delivered to your door!
