#Non-local modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.chrome.options import Options as _chrome_options
from selenium.webdriver.firefox.options import Options
from time import sleep

def browser(user_browser, headless):
    """Specifies selenium browser from the following choices:
    'Chrome',
    'Firefox',
    'Edge'"""
    global _headless, driver
    _headless = headless
    driver = user_browser


def menu(item):
    class InvalidMenuOption(Exception):
        pass
    def __menu__(item):
        if item == "Pizza":
            print('PEP = Pepperoni Pizza\nSAU = Sausage Pizza\nMCP = Medium Cheese Pizza\nCP = Cheese Pizza\nSH = Super Hawaiian Pizza\nGF = Garden Fresh Pizza\nFSTA = Fresh Spinach & Tomato Alfred Pizza')
        elif item == "Drinks":
            print("2LP = 2 Liter Pepsi $3.00\n20OZP = 20 Ounce Pepsi $2.00\n2LMD = 2 Liter Mountain Dew $3.00\n20OZMD = 20 Ounce Mountain Dew $2.00\n20OZDMD = 20 Ounce Diet Mountain Dew $2.00\n2LDP = 2 Liter Diet Pepsi")
        elif item == "Deserts":
            print('CPA = Cinnamon Pull Aparts\nCCC = Chocolate Chip Cookie\nDCCB = Chocolate Chip Brownie')
        elif item == "Sides":
            print("")
        else:
            raise InvalidMenuOption('Searched item is not a Papa Johns menu item.')
    __menu__(item)

def payment(*args, **kwargs):
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
    def __order__(user_order, user_driver, headless, real_number, real_street, real_city, real_state, real_zipcode, _first_name, _last_name, _email, _phonenum, *args, **kwargs):
        credit_number = kwargs.get('credit_number', None)
        name_on_card = kwargs.get('name_on_card', None)
        exp_month = kwargs.get('exp_month', None)
        exp_year = kwargs.get('exp_year', None)
        sec_code = kwargs.get('sec_code', None)
        cash = kwargs.get('cash_option', None)
        type_of_user_order = str(type(user_order))
        if type_of_user_order != "<class 'list'>":
            raise TypeError('Your order must be a list.')
        else:
            chrome_options = _chrome_options()
            chrome_options.add_argument("--headless")
            fireFoxOptions = Options()
            fireFoxOptions.headless = True
            if user_driver == 'Chrome':
                if headless == True:
                    driver = webdriver.Chrome(options=chrome_options)
                else:
                    driver = webdriver.Chrome()
            if user_driver == 'Firefox':
                if headless == True:
                    driver = webdriver.Firefox(options=fireFoxOptions)
                else:
                    driver = webdriver.Firefox()
            if user_driver == 'Edge':
                if headless == True:
                    raise Exception('Selenium driver cannot be headless and Edge.')
                else:
                    driver = webdriver.Edge()
            driver.get("https://www.papajohns.com/")
            order_button = driver.find_element_by_class_name('nav-main-link')
            order_button.click()
            sleep(1)
            pizzafinder = driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/section[1]/div/div/ul/li[4]/div/form/div[2]/a')
            pizzafinder.click()
            sleep(1)
            user_address = driver.find_element_by_xpath('//*[@id="autocomplete"]')
            user_address.send_keys(real_number, real_street, ',', real_city, ',', real_state, 'USA')
            sleep(1)
            user_zipcode = driver.find_element_by_xpath('//*[@id="locations-usa-zipcode"]')
            user_zipcode.send_keys(real_zipcode)
            sleep(1)
            user_zipcode.send_keys(Keys.RETURN)
            sleep(3)
            user_close = driver.find_element_by_css_selector("a.button:nth-child(2)")
            sleep(1)
            user_close.click()
            sleep(1)
            pizza_button = '.subnavigation--horizontal > li:nth-child(1) > a:nth-child(1)'
            #drinks_button = 'body > div.page-wrapper > main > div.container.spacing-top-sm.spacing-bottom-med > nav > ul > li:nth-child(5) > a'
            for step in user_order:
                if step == 'PEP':
                    button = driver.find_element_by_css_selector(pizza_button)
                    button.click()
                    pizza = driver.find_element_by_css_selector('section.spacing-bottom-med:nth-child(2) > div:nth-child(2) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(7) > button:nth-child(1)')
                    pizza.click()
                elif step == 'CP':
                    button = driver.find_element_by_css_selector(pizza_button)
                    button.click()
                    pizza = driver.find_element_by_css_selector('section.spacing-bottom-med:nth-child(2) > div:nth-child(2) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > form:nth-child(2) > div:nth-child(7) > button:nth-child(1)')
                    pizza.click()
                elif step == 'SAU':
                    button = driver.find_element_by_css_selector(pizza_button)
                    button.click()
                    pizza = driver.find_element_by_css_selector('section.spacing-bottom-med:nth-child(2) > div:nth-child(2) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(3) > div:nth-child(1) > form:nth-child(2) > div:nth-child(7) > button:nth-child(1)')
                    pizza.click()
                elif step == 'SH':
                    button = driver.find_element_by_css_selector(pizza_button)
                    button.click()
                    pizza = driver.find_element_by_css_selector('section.spacing-bottom-med:nth-child(3) > div:nth-child(2) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > form:nth-child(2) > div:nth-child(7) > button:nth-child(1)')
                    pizza.click()
                elif step == 'GF':
                    button = driver.find_element_by_css_selector(pizza_button)
                    button.click()
                    pizza = driver.find_element_by_css_selector('section.spacing-bottom-med:nth-child(4) > div:nth-child(2) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(3) > div:nth-child(1) > form:nth-child(2) > div:nth-child(7) > button:nth-child(1)')
                    pizza.click()
                elif step == 'FSTA':
                    button = driver.find_element_by_css_selector(pizza_button)
                    button.click()
                    pizza = driver.find_element_by_css_selector('section.spacing-bottom-med:nth-child(4) > div:nth-child(2) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(7) > button:nth-child(1)')
                    pizza.click()
                checkout = driver.find_element_by_xpath('//*[@id="cart"]')
                checkout.click()
                confirm = driver.find_element_by_xpath('/html/body/div[2]/main/div/div[2]/div/form/button')
                confirm.click()
                sleep(1)
                popup = driver.find_element_by_css_selector('a.button')
                popup.click()    
                if cash == True:
                    cashoption = driver.find_element_by_css_selector('#cashPayment > a:nth-child(1)')
                    cashoption.click()
                else:
                    credit_box = driver.find_element_by_xpath('//*[@id="credit-card-number"]')
                    credit_box.send_keys(credit_number)
                    card_name_box = driver.find_element_by_xpath('//*[@id="credit-card-name"]')
                    card_name_box.send_keys(name_on_card)
                    exp_month_dropdown = Select(driver.find_element_by_xpath('//*[@id="credit-card-expiration-month"]'))
                    if exp_month == 'January':
                        exp_month_dropdown.select_by_visible_text('01 - January')
                    elif exp_month == 'Febuary':
                        exp_month_dropdown.select_by_visible_text('02 - February')
                    elif exp_month == 'March':
                        exp_month_dropdown.select_by_visible_text('03 - March')
                    elif exp_month == 'April':
                        exp_month_dropdown.select_by_visible_text('04 - April')
                    elif exp_month == 'May':
                        exp_month_dropdown.select_by_visible_text('05 - May')
                    elif exp_month == 'June':
                        exp_month_dropdown.select_by_visible_text('06 - June')
                    elif exp_month == 'July':
                        exp_month_dropdown.select_by_visible_text('07 - July')
                    elif exp_month == 'August':
                        exp_month_dropdown.select_by_visible_text('08 - August')
                    elif exp_month == 'September':
                        exp_month_dropdown.select_by_visible_text('09 - September')
                    elif exp_month == 'October':
                        exp_month_dropdown.select_by_visible_text('10 - October')
                    elif exp_month == 'November':
                        exp_month_dropdown.select_by_visible_text('11 - November')
                    elif exp_month == 'December':
                        exp_month_dropdown.select_by_visible_text('12 - December')
                    exp_year_dropdown = Select(driver.find_element_by_xpath('//*[@id="credit-card-expiration-year"]'))
                    exp_year_dropdown.select_by_visible_text(exp_year)
                    credit_zipcode = driver.find_element_by_xpath('//*[@id="billing-zipcode"]')
                    credit_zipcode.send_keys(real_zipcode)
                    sec_code_box = driver.find_element_by_xpath('//*[@id="credit-card-cvv"]')
                    sec_code_box.send_keys(sec_code)
                fname = driver.find_element_by_xpath('//*[@id="contact-firstname"]')
                fname.send_keys(_first_name)
                lname = driver.find_element_by_xpath('//*[@id="contact-lastname"]')
                lname.send_keys(_last_name)
                sleep(1)
                email = driver.find_element_by_xpath('//*[@id="contact-email"]')
                email.send_keys(_email)
                phonenum = driver.find_element_by_xpath('//*[@id="phone-number"]')
                phonenum.send_keys(_phonenum)
                sleep(1)
                leaveorderatdoor = driver.find_element_by_xpath('//*[@id="touchlessFlag"]')
                leaveorderatdoor.click()
                #TODO Make an option to add a tip.
                #tip_box = driver.find_element_by_xpath('//*[@id="tipCustom"]')
                #tip_box.send_keys(tip)
                termscond = driver.find_element_by_xpath('//*[@id="input"]')
                termscond.click()
                sleep(1)
                revieworder = driver.find_element_by_xpath('//*[@id="validate-order"]')
                revieworder.click()
                checkoutbutton = driver.find_element_by_xpath('//*[@id="place-your-order"]')
                checkoutbutton.click()
                driver.close()
    """Provide the items off the menu that the user will order. Refer to item codes.
    Order be type list."""
    if _cash and _headless:
        __order__(user_order, driver, True, _number, _street, _city, _state, _zipcode, _first_name, _last_name, _email, _phone_number, cash_option=True)
    elif _cash and not _headless:
        __order__(user_order, driver, False, _number, _street, _city, _state, _zipcode, _first_name, _last_name, _email, _phone_number, cash_option=True)
    elif not _cash and _headless:
         __order__(user_order, driver, True, _number, _street, _city, _state, _zipcode, _first_name, _last_name, _email, _phone_number, credit_number=_credit_card_number, name_on_card=_name_on_card, exp_month=_exp_month, exp_year=_exp_year, sec_code=_security_code)
    elif not _cash and not _headless:
        __order__(user_order, driver, False, _number, _street, _city, _state, _zipcode, _first_name, _last_name, _email, _phone_number, credit_number=_credit_card_number, name_on_card=_name_on_card, exp_month=_exp_month, exp_year=_exp_year, sec_code=_security_code)
