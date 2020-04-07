from Utilities.PageBase import PageBase
import appium.webdriver.webelement
from MobilePageObjects.Mobile_Thanks import MobileThanks
import MobileLocators.MobileCheckoutLocators as loc
import Static.Constants as const
import logging
import Utilities.CustomLogger as cl
log = cl.customLogger(logging.INFO)
from selenium.webdriver.common.keys import Keys
from datetime import date
import time

class MobileCheckout(PageBase):
    '''
    Class for methods of Checkout Page of mobile view
    '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_more_items(self):
        '''
        Method to click on Add More Items button
        '''
        try:
            log.info("Clicking on Add More Items button")
            self.wait_till_element_is_present(loc.add_more_items)
            self.click(loc.add_more_items)
        except Exception as e:
            raise Exception("Unable to click on Add More Items due to "+str(e))

    def click_add_to_order(self):
        '''
        Method to click on Add to Order button
        '''
        try:
            log.info("Clicking on Add to order button ")
            self.wait_till_element_is_present(loc.add_to_order)
            self.click(loc.add_to_order)
        except Exception as e:
            raise Exception("Unable to click on Add to order button due to "+str(e))

    def select_flavours(self,flavour):
        '''
        Method to Select ice cream flavours
        '''
        try:
            log.info("Clicking on Select Ice Cream flavours dropdown")
            self.wait_till_element_is_present(loc.select_flavours)
            log.info("Selecting the flavour "+ flavour + " from the options")
            self.select_dropdown_option(loc.select_flavours,flavour)
        except Exception as e:
            raise  Exception ("Unable to Select the flavour due to "+str(e))

    def enter_recipient_name(self,name):
        '''
        Method to enter the recipient full name
        '''
        try:
            log.info("Clicking the input box to enter the recipient's full name")
            log.info("Entering the full name"+ name)
            self.wait_till_element_is_present(loc.recipient_full_name_input)
            self.send_keys(loc.recipient_full_name_input,name)

        except Exception as e:
            raise Exception ("Unable to enter the recipient's full name due to "+str(e))

    def click_form(self,locator):
        try:
            self.wait_till_element_is_present(locator)
            self.click()
        except Exception as e:
            raise Exception ("Unable to click" + str(e))

    def enter_recipient_phone_number(self,number):
        '''
        Method to enter the recipient's phone number
        '''
        try:
            log.info("Clicking the phone number input boc")
            log.info("Entering the phono number "+ str(number))
            self.wait_till_element_is_present(loc.recipient_phone_number_input)
            self.send_keys(loc.recipient_phone_number_input,number)
            self.hide_keyboard()
        except Exception as e:
            raise Exception ("Unable to enter the recipient's phone number "+str(e))

    def enter_recipient_extension(self,ext):
        '''
        Method to enter the recipient's extension number
        '''
        try:
            log.info("Clicking the extension input box")
            log.info("Entering the extension number "+ str(ext))
            self.wait_till_element_is_present(loc.recipient_extension_input)
            self.send_keys(loc.recipient_extension_input,str(ext))
        except Exception as e:
            raise Exception ("Unable to enter the recipient's extension number due to "+str(e))


    def enter_recipient_secondary_address(self,address):
        '''
        Method to enter the recipient's secondary address
        '''
        try:
            log.info("Clicking the secondary address input box")
            log.info("Entering the secondary address ")
            self.send_keys(loc.recipient_secondary_address_input,address)
        except Exception as e:
            raise Exception("Unable to enter the secondary address od recipient due to "+str(e))

    def click_deliver_to_door_chkbx(self):
        '''
        Method to click the deliver to my door checkbox
        '''
        try:
            self.wait_till_element_is_present(loc.deliver_to_my_door_chkbx)
            log.info("Clicking the Deliver to my door checkbox")
            self.click(loc.deliver_to_my_door_chkbx)
        except Exception as e:
            raise Exception ("Unable to click the Deliver to my door checkbox due to "+str(e))

    def click_meet_me_outside(self):
        '''
        Method to click the meet me outside checkbox
        '''
        try:
            self.wait_till_element_is_present(loc.meet_me_outside_chkbx)
            log.info("Clicking the meet me outside checkbox")
            time.sleep(3)
            self.click(loc.meet_me_outside_chkbx)
        except Exception as e:
            raise Exception ("Unable to click on meet me outside due to "+str(e))

    def leave_order_at_door(self):
        '''
        Method to click on Leave order at my door
        '''
        try:
            log.info("Clicking the leave order at my door checkbox")
            self.click(loc.leave_order_at_door_chkbx)
        except Exception as e:
            raise Exception ("Unable to click  leave order at door checkbox due to "+str(e))

    def enter_delivery_instructions(self,message):
        '''
        Method to enter the delivery instructions
        '''
        try:
            log.info("Entering the delivery instruction message")
            self.send_keys(loc.delivery_message_input,message)
        except Exception as e:
            raise Exception ("Unable to enter the delivery instruction due to "+str(e))

    def scroll_down(self, locator, wait_time=2):
        """
        Scroll down WebPage
        :param locator: locator
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.PAGE_DOWN)
            self.sleep_in_seconds(wait_time)
            # element.send_keys(Keys.PAGE_DOWN)
            # self.sleep_in_seconds(wait_time)
        except Exception as e:
            raise e


    def enter_recpient_instructions(self,message):
        '''
        Method to enter the recipient isntructions
        '''
        try:
            log.info("Entering the recipient instruction message")
            self.send_keys(loc.recipient_message_input,message)
        except Exception as e:
            raise Exception ("Unable to enter the recipient instruction message due to "+str(e))

    def click_same_as_above_chkbx(self):
        '''
        Method to click on same as above checkbox
        '''
        try:
            log.info("Clicking rhe same as above checkbox")
            self.click(loc.same_as_above_chkbx)
        except Exception as e:
            raise Exception ("Unable to click on same as above checkbox due to"+str(e))

    def enter_customer_name(self, name):
        '''
        Method to enter the customer full name
        '''
        try:
            log.info("Clicking the input box to enter the customer's full name")
            log.info("Entering the full name" + name)
            self.send_keys(loc.customer_full_name_input, name)
        except Exception as e:
            raise Exception("Unable to enter the recipient's full name due to " + str(e))

    def enter_customer_phone_number(self, number):
        '''
        Method to enter the customer's phone number
        '''
        try:
            log.info("Clicking the phone number input boc")
            log.info("Entering the phono number " + str(number))
            self.send_keys(loc.customer_phone_number_input, number)
            self.hide_keyboard()
        except Exception as e:
            raise Exception("Unable to enter the customer's phone number " + str(e))

    def enter_customer_phone_number_extension(self, ext):
        '''
        Method to enter the customer's extension number
        '''
        try:
            log.info("Clicking the extension input box")
            log.info("Entering the extension number " + str(ext))
            self.send_keys(loc.customer_extenstion_input, str(ext))
        except Exception as e:
            raise Exception("Unable to enter the recipient's extension number due to " + str(e))

    def enter_customer_email_id(self,email):
        '''
        Method to enter the customer's email id
        '''
        try:
            self.wait_till_element_is_present(loc.customer_email_input)
            log.info("Entering the email id of the customer")
            self.sleep_in_seconds(5)
            self.send_keys(loc.customer_email_input,email)
            self.hide_keyboard()
        except Exception as e:
            raise Exception("Unable to enter the customer email id due to "+str(e))

    def click_continue_as_guest(self):
        '''
        Method to click continue as guest
        '''
        try:
            log.info("Clicking the continue as guest radio button")
            self.click(loc.continue_as_guest_radio_btn)
        except Exception as e:
            raise Exception ("Unable to click the continue as guest radio button due to "+str(e))

    def click_register_after_checkout(self):
        '''
        Method to click on Register after checkout radio button
        '''
        try:
            log.info("Clicking on Register After checkout radio button")
            self.click(loc.register_after_checkout_radio_btn)
        except Exception as e:
            raise Exception("Unable to click on register after checkout radio button due to "+str(e))

    def click_already_registered(self):
        '''
        Method to click already registered radio button
        '''
        try:
            log.info("Clicking on Already Registerd radio button")
            self.click(loc.already_registered_radio_btn)
        except Exception as e:
            raise Exception ("Unable to click on Already registered radio button due to "+str(e))

    def click_credit_card(self):
        '''
        Method to click on credit card payment method
        '''
        try:
            log.info("Clicking on Credit card payment method")
            self.click(loc.credit_card_btn)
        except Exception as e:
            raise Exception("Unable to click on credit card button due to "+str(e))

    def enter_name_credit_card(self,name):
        '''
        Method to enter the Name on credit card
        '''
        try:
            log.info("Entering the Name on Credit card")
            self.send_keys(loc.credit_card_name,name)
            self.hide_keyboard()
        except Exception as e:
            raise Exception("Unable to Enter the name on credit card due to "+str(e))

    def enter_credit_card_number(self,number):
        '''
        Method to enter the credit card number
        '''
        try:
            log.info("Entering the credit card number")
            self.send_keys(loc.credit_card_number,number)
            self.hide_keyboard()
        except Exception as e:
            raise Exception ("Unable to enter the credit card number due to "+str(e))

    def enter_credit_card_expiry(self,exp_date):
        '''
        Method to enter the credit card expiry date
        '''
        try:
            log.info("Entering the credit card expiration date")
            self.send_keys(loc.credit_card_expiry,exp_date)
            self.hide_keyboard()
        except Exception as e:
            raise Exception ("Unable to enter the credit card expiration date due to "+str(e))

    def enter_credit_card_cvc(self,cvc):
        '''
        Method to enter the Credit Card CVC code
        '''
        try:
            log.info("Entering the credit card CVC Code")
            self.send_keys(loc.credit_card_cvc,cvc)
            self.hide_keyboard()
        except Exception as e:
            raise  Exception ("Unable to enter the Credit card CVC due to "+str(e))

    def enter_credit_card_postal_code(self,code):
        '''
        Method to enter the credit cad postal code
        '''
        try:
            log.info("Entering the postal code for credit card")
            self.send_keys(loc.credit_card_postal_code,code)
        except Exception as e:
            raise Exception ("Unable to enter the credit card postal code due to "+str(e))

    def select_tip_from_dropdown(self,tip):
        '''
        Method to enter the tip
        '''
        try:
            log.info("Selecting the tip from dropdown")
            self.select_value_from_dropdown(loc.tip_dropdown,tip)
        except Exception as e:
            raise Exception("Unable to select tip from dropdown due to "+str(e))

    def click_place_order(self):
        '''
        Method to click on Place order button
        '''
        try:
            log.info("Clicking on Place order button")
            self.click(loc.place_order_btn)
            return MobileThanks(self.driver)
        except Exception as e :
            raise Exception ("Unable to click on Place order button due to "+str(e))