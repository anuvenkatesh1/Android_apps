'''
Created on Oct 5, 2017

@author: Anu

Connect android device via USB
In the developer tools turn USB Debugging ON
Start the UI Atomator Viewer from Android SDK
In the Android device, open up calculator app
Click Device screenshot in the UI Atomator Viewer to capture the device screenshot 
 to enable inspection of elements in the viewer

'''
import unittest
from appium import webdriver
import os
import time


class Android_Calculator_Test(unittest.TestCase):


    def setUp(self):
        desired_caps = {}

        desired_caps['platformName'] = 'Android'
        
        #Can be found from the About Phone in your android device

        desired_caps['platformVersion'] = '4.4.3'
        
        #type adb devices from command prompt to list the connected devices
        
        #the below device name is used for real device connected to the PC
        '''desired_caps['deviceName'] = 'TA8830GUHM' '''
        
        desired_caps['deviceName'] = '192.168.217.101:5555'
        desired_caps['BROWSER_NAME'] = ''
        
        # Install APK info on your android device, open it, hold it on the AUT for few secs, open 
        # detailed information, find the package and activity names there
        
        desired_caps['appPackage'] = 'com.android.calculator2'

        desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        

    def test_calculator(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        
        #clear old result first
        btn = driver.find_elements_by_class_name('android.widget.Button')[0]
        btn.click()
        
        driver.find_element_by_name('5').click()
        driver.find_element_by_id('com.android.calculator2:id/plus').click()
        driver.find_element_by_name('2').click()
        driver.find_element_by_id('com.android.calculator2:id/equal').click()
        
        #result
        result = driver.find_element_by_class_name('android.widget.EditText').text
        print "The result is:" + result
        
         
        pass
    
    
    def tearDown(self):
        
        # tear down the test
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()