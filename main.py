# Python imports
# argument parser for command line arguments
import argparse
import sys
import time

from selenium import webdriver

# handle command line arguments
parser = argparse.ArgumentParser(
    description='Simple example with Selenium -- running Firefox'
)

parser.add_argument(
    '-l', '--headless',
    help='Run Firefox in headless mode',
    action='store_true',
)
args = parser.parse_args()
# prepare options for Firefox browser
options = webdriver.FirefoxOptions()
options.headless = args.headless

# instantiate the browser
browser = webdriver.Firefox(firefox_options=options)
browser.get('https://www.ffdm.cz')
# wait one tenth of a second
time.sleep(0.1)
# find the Program button in the menu
program_btn = browser.find_element_by_id('menu-item-5224')
# wait for one second, because the JS might still be loading and
# making the button obsucre/unclickable
time.sleep(1)
program_btn.click()
# to verify, that it actually works
cur_url = browser.current_url
# free up resource
browser.close()

if cur_url == 'https://www.ffdm.cz/program/':
    print('Happy')
    sys.exit(0)

print('Sad')
sys.exit(1)
