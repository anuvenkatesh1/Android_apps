'''
Created on Oct 17, 2017

@author: labinav
'''
import unittest
from appium import webdriver
import os
import time
from lib2to3.tests.support import driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Android_Mobile_Web_Test(unittest.TestCase):


    def setUp(self):
        desired_caps = {}

        desired_caps['platformName'] = 'Android'
        
        #Can be found from the About Phone in your android device

        desired_caps['platformVersion'] = '4.4.3'
        
        #type adb devices from command prompt to list the connected devices
        
        #the below device name is used for real device connected to the PC
        desired_caps['deviceName'] = 'TA8830GUHM'
        
        #emulator device name - run adb devices once emulated device is started
       # '''desired_caps['deviceName'] = '192.168.217.101:5555'''
        desired_caps['BROWSER_NAME'] = 'CHROME'
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        pass


    def tearDown(self):
        self.driver.quit()
        pass
    
    def isElementPresent(self, locator):
        try:
            self.driver.find_element_by_name(locator)
            print 'Element found'
        except NoSuchElementException:
            print ('No such thing')
            return False
        return True


    def test_fbLogin(self):
        driver = self.driver
        driver.implicitly_wait(30)
        
        driver.get("http://www.facebook.com")
        print "title" + driver.title
        
        driver.find_element_by_name("email").send_keys("something@gmail.com")
  
        if self.isElementPresent('pass'):
            print 'we are in if'
            driver.find_element_by_name("pass").send_keys("fake_pw")
    
        driver.find_element_by_name("login").click()
        
        driver.implicitly_wait(30)
        
        #in the page following, click on Not Now
        driver.find_element_by_xpath("//a[contains(@href,'regular_login')]").click()
        #time.sleep(5)
        #WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID,"element")))
        action = ActionChains(driver)
        time.sleep(5)
        print driver.title
        self.assertEquals('Facebook', driver.title, 'Title Facebook not found')
       
        action.move_by_offset(500, 500).double_click().perform()
        #self.driver.execute_script('el = document.elementFromPoint(440, 120); el.click();')
        print 'clicked'
        
        driver.switch_to.default_content()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//textarea[contains(text(),'What's on your mind?')]")),'element not found')
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_fbLogin']
    unittest.main()
