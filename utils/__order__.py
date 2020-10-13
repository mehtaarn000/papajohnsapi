from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.chrome.options import Options as _chrome_options
from selenium.webdriver.firefox.options import Options
from time import sleep

def __order__(user_order, driver, real_number, real_street, real_city, real_state, real_zipcode, _first_name, _last_name, _email, _phonenum, *args, **kwargs):
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
        driver = webdriver.Firefox()
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
            #FIXME Make sure to uncomment these last three lines
            #checkoutbutton = driver.find_element_by_xpath('//*[@id="place-your-order"]')
            #checkoutbutton.click()
            #driver.close()
