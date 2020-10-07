#Non-local modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.chrome.options import Options as _chrome_options
from selenium.webdriver.firefox.options import Options
from time import sleep

#Local modules
from __browser__ import __browser__
from __menu__ import __menu__
import __errors__
from __order__ import __order__
#from __search__ import __search__
#from __coupons__ import __coupons__
#from __special_instructions__ import __special_instructions__

def browser(user_browser, headless):
    """Specifies selenium browser from the following choices:
    'Chrome',
    'Firefox',
    'Edge'"""
    global driver
    driver = __browser__(user_browser, headless)
    return driver

def menu(item):
    """Locate food and drink items on menu, and their order codes.
    Options:
    'Pizza',
    'Drinks',
    'Deserts',
    'Sides'"""
    __menu__(item)

def credit_card(*args, **kwargs):
    """Confirm payment method
    If cash, then 'cash=True'
    If credit card, then:
    provide credit card number, 
    name on card, 
    expiration month, 
    expiration year, 
    and security code"""
    global _credit_card_number, _name_on_card, _exp_month, _exp_year, _security_code, _cash
    _cash = kwargs.get('cash', None)
    _credit_card_number = kwargs.get('credit_card_number', None)
    _name_on_card = kwargs.get('name_on_card', None)
    _exp_month = kwargs.get('exp_month', None)
    _exp_year = kwargs.get('exp_year', None)
    _security_code = kwargs.get('security_code', None)

def address(number, street, city, state, zipcode):
    """Input address:
    House number,
    Street,
    City,
    State,
    Zipcode"""
    global _number, _street, _city, _state, _zipcode
    _number = number
    _street = street
    _city = city
    _state = state
    _zipcode = zipcode

def user(first_name, last_name, phone_number, email):
    """Input information about the user:
    First name,
    Last name,
    Phone Number,
    Email"""
    global _first_name, _last_name, _phone_number, _email
    _first_name = first_name
    _last_name = last_name
    _phone_number = phone_number
    _email = email


def order(user_order):
    """Provide the items off the menu that the user will order. Refer to item codes.
    Must be type list."""
    if _cash:
        __order__(user_order, driver, _number, _street, _city, _state, _zipcode, _first_name, _last_name, _email, _phone_number, cash_option=True)
    else:
        __order__(user_order, driver, _number, _street, _city, _state, _zipcode, _first_name, _last_name, _email, _phone_number, credit_number=_credit_card_number, name_on_card=_name_on_card, exp_month=_exp_month, exp_year=_exp_year, sec_code=_security_code)
