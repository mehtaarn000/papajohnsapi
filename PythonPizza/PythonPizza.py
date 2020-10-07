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
global _cash
def browser(user_browser, headless):
    global driver
    driver = __browser__(user_browser, headless)
    return driver

def menu(item):
    __menu__(item)

def credit_card(credit_card_number, name_on_card, exp_month, exp_year, security_code):
    global _credit_card_number, _name_on_card, _exp_month, _exp_year, _security_code
    global _cash
    _cash = False
    _credit_card_number = credit_card_number
    _name_on_card = name_on_card
    _exp_month = exp_month
    _exp_year = exp_year
    _security_code = security_code

def cash():
    global _cash
    _cash = True

def address(number, street, city, state, zipcode):
    global _number, _street, _city, _state, _zipcode
    _number = number
    _street = street
    _city = city
    _state = state
    _zipcode = zipcode

def user(first_name, last_name, phone_number, email):
    global _first_name, _last_name, _phone_number, _email
    _first_name = first_name
    _last_name = last_name
    _phone_number = phone_number
    _email = email


def order(user_order):
    if True == True:
        __order__(user_order, driver, _number, _street, _city, _state, _zipcode, _first_name, _last_name, _email, _phone_number, cash_option=True)
    #elif _cash == False:
    #    __order__(user_order, driver, _number, _street, _city, _state, _zipcode, _first_name, _last_name, _email, _phone_number, credit_number=_credit_card_number, name_on_card=_name_on_card, exp_month=_exp_month, exp_year=_exp_year, sec_code=_security_code)
    