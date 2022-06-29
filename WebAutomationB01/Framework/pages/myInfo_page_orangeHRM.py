import time

from selenium.webdriver.common.by import By


class MyInfoPage_orange():

    def __init__(self, driver):
        self.driver = driver

    def emergency_contact_add(self, contact_name, relation, home_telephone_number, mobile_number,
                              work_telephone_number):
        # Open MyInfo
        my_info = self.driver.find_element(By.LINK_TEXT, 'My Info')
        my_info.click()
        time.sleep(3)

        # Emergency Contact
        emergency_contact = self.driver.find_element(By.LINK_TEXT, 'Emergency Contacts')
        emergency_contact.click()
        time.sleep(2)

        # Add contract
        add_button = self.driver.find_element(By.ID, "btnAddContact")
        add_button.click()
        time.sleep(2)

        name = self.driver.find_element(By.NAME, 'emgcontacts[name]')
        name.send_keys(contact_name)

        relationship = self.driver.find_element(By.NAME, 'emgcontacts[relationship]')
        relationship.send_keys(relation)

        home_telephone = self.driver.find_element(By.NAME, 'emgcontacts[homePhone]')
        home_telephone.send_keys(home_telephone_number)

        mobile = self.driver.find_element(By.NAME, 'emgcontacts[mobilePhone]')
        mobile.send_keys(mobile_number)

        work_telephone = self.driver.find_element(By.NAME, 'emgcontacts[workPhone]')
        work_telephone.send_keys(work_telephone_number)

        save_button = self.driver.find_element(By.ID, 'btnSaveEContact')
        save_button.click()

    def emergency_contact_edit(self, contact_name, relation, home_telephone_number, mobile_number,
                               work_telephone_number):
        # Open added contact
        added_contact_name = self.driver.find_element(By.LINK_TEXT, 'NY1001')
        added_contact_name.click()
        time.sleep(3)

        name = self.driver.find_element(By.NAME, 'emgcontacts[name]')
        name.clear()
        name.send_keys(contact_name)

        relationship = self.driver.find_element(By.NAME, 'emgcontacts[relationship]')
        relationship.clear()
        relationship.send_keys(relation)

        home_telephone = self.driver.find_element(By.NAME, 'emgcontacts[homePhone]')
        home_telephone.clear()
        home_telephone.send_keys(home_telephone_number)

        mobile = self.driver.find_element(By.NAME, 'emgcontacts[mobilePhone]')
        mobile.clear()
        mobile.send_keys(mobile_number)

        work_telephone = self.driver.find_element(By.NAME, 'emgcontacts[workPhone]')
        work_telephone.clear()
        work_telephone.send_keys(work_telephone_number)

        save_button = self.driver.find_element(By.ID, 'btnSaveEContact')
        save_button.click()

    def emergency_contact_delete(self):
        delete_button = self.driver.find_element(By.ID, 'delContactsBtn')
        delete_button.click()

    '''
    def attachment_add(self):
        
    def attachment_delete(self):
    
    '''
