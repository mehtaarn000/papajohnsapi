# papajohnsapi
A Python module that will allow users to use selenium to order pizza from Papa Johns.

## Requirements
`pip install selenium`
If you are using the Chrome Browser, download the compatible version of the chromedriver [here](https://chromedriver.chromium.org/).
If you are using the Firefox Browser, download the compatible version of the geckodriver [here](https://github.com/mozilla/geckodriver/releases).
On OSX make sure to move either of these drivers to `/usr/local/bin` with either:
`mv geckodriver /usr/local/bin`
or 
`mv chromedriver /usr/local/bin`

## Installation
`pip install PythonPizza`

## Usage
First, import the module after downloading with:
`import PythonPizza as pizza`

Specify your choice of browser and the choice of going headless (You won't see a browser window) with:
`pizza.browser('Firefox', headless=False)`
Replace arguments as needed.

Specify your address with:
`pizza.address(house number, street, city, state(in 2 letter form), zipcode)`
Replace arguments as needed.

Specify who you want ordering with:
`pizza.user(first name, last name, phone number, email)`
Replace arguments as needed.

Check the menu with:
`pizza.menu(item)`
This item can be: 'Pizza', 'Drinks', 'Sides', or 'Desserts'
(Currently you can only order pizza)
Replace Arguments as needed

Then, place your order with:
`pizza.order([items])`
Replace `items` with the order codes provided by:
`pizza.menu(item)`

Finally, kick back as you get fresh pizza delivered to your door!
