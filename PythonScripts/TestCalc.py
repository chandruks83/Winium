from selenium import webdriver
import time
import os
os.startfile(r'C:\Users\Chandru\PycharmProjects\Winium\WiniumDriver\Winium.Desktop.Driver.exe')
driver = webdriver.Remote(command_executor='http://localhost:9999',
    desired_capabilities={
        "debugConnectToRunningApp": 'false',
        "app": r"C:/windows/system32/calc.exe"
    })
window = driver.find_element_by_name('Calculator')
window.find_element_by_name('Five').click()
window.find_element_by_name('Two').click()
window.find_element_by_name('Plus').click()
window.find_element_by_name('Four').click()
window.find_element_by_name('Eight').click()
window.find_element_by_name('Equals').click()
result = window.find_element_by_id('CalculatorResults').get_attribute('Name')
print(result)
window.find_element_by_name('Close').click()
os.system('TASKKILL /F /IM Winium.Desktop.Driver.exe')