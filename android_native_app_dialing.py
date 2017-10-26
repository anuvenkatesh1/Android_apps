'''
Created on Oct 20, 2017

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
from selenium.webdriver.common import by


class Android_NativeTest(unittest.TestCase):


    def setUp(self):
        desired_caps = {}

        desired_caps['platformName'] = 'Android'
        
        #Can be found from the About Phone in your android device

        desired_caps['platformVersion'] = '4.4.3'
        
        #type adb devices from command prompt to list the connected devices
        
        #the below device name is used for real device connected to the PC
        #desired_caps['deviceName'] = 'TA8830GUHM'
        
        #emulator device name - run adb devices once emulated device is started
        desired_caps['deviceName'] = '192.168.217.101:5555'
        
        #for native app testing no need for browser name
        desired_caps['BROWSER_NAME'] = ''
        #desired_caps['BROWSER_NAME'] = 'CHROME'
        
        '''
        To get the package and activity name: adb shell > run dumpsys command (or)
        adb logcat > open app in phone/emulator > press ctl+c (or)
        adb shell >  run pull command to pull apk files from emulator/phone (or)
        apk info app (on real device) > locate the app > press on it for fews > view detailed information
        
        '''
        desired_caps['appPackage'] = 'com.android.dialer'

        desired_caps['appActivity'] = 'com.android.dialer.DialtactsActivity'
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        pass


    def tearDown(self):
        self.driver.quit()
        pass


    def test_dialing(self):
        driver=self.driver
        
        #open dialer
        driver.find_element_by_name("Phone")
        #time.sleep(5)
        
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'com.android.dialer:id/dialButton')),'dialer not found')
        
        #enter phone number
        #'name' is either the 'text' or 'content-desc' property
        driver.find_element_by_name('four').click()
        driver.find_element_by_name('zero').click()
        driver.find_element_by_name('eight').click()
        driver.find_element_by_name('two').click()
        driver.find_element_by_name('zero').click()
        driver.find_element_by_name('four').click()
        driver.find_element_by_name('four').click()
        driver.find_element_by_name('two').click()
        driver.find_element_by_name('eight').click()
        driver.find_element_by_name('four').click()
        driver.find_element_by_id('com.android.dialer:id/dialButton').click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'End')),'End button not found')
        driver.find_element_by_name('End').click()
        
        time.sleep(5)
        
        
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()