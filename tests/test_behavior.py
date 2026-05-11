"""
Tests for CSS styles across a few pages.

Selenium webdriver for Chrome (a.k.a. the file named chromedriver) must be installed in either:
- in the same directory as chrome.exe on Windows (e.g. C:\Program Files\Google\Chrome\Application)
- in a directory that is included in the PATH on Mac OS X (e.g. /usr/local/bin)
"""

import pytest
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Tests:

  @pytest.fixture(scope="class")
  def settings(self):
    settings = json.load(open('./settings.json', 'r'))
    yield settings

  @pytest.fixture(scope="class", )
  def driver(self, settings):
    """
    Pop open a web browser and make it available to the tests.
    """

    # set up the fixture
    page = 'topic_of_interest.html'
    url = "{}/{}".format(settings["site_url"], page)
    driver = webdriver.Chrome()
    driver.get(url) # load the site from the settings file
    # provide the fixture value
    yield driver  
    # now tear it down
    driver.close()

  def test_image_swap(self, driver, settings):
    """
    Check for a valid image swap, where the img tag's src attribute changes on mouseover and reverts on mouseout.
    """
    # grab necessary elements for interaction
    jquery_settings = settings["jquery_settings"]["image_swap"]
    target = driver.find_element_by_css_selector(jquery_settings["trigger_element_selector"])
    
    # get the original text before interaction
    original_src = target.get_attribute('src')

    # mouse over
    ActionChains(driver).move_to_element(target).perform()
    
    # grab the new src
    mouseover_src = target.get_attribute('src')

    # mouse out
    # grab some other element
    other_el = driver.find_element_by_tag_name('body')
    ActionChains(driver).move_to_element(other_el).perform() 

    # grab the new src after interaction
    mouseout_src = target.get_attribute('src')

    assert original_src != mouseover_src
    assert original_src == mouseout_src

  def test_content_change(self, driver, settings):
    """
    Check that the text content within the target element changes after the event occurs.
    """
    # grab necessary elements for interaction
    jquery_settings = settings["jquery_settings"]["content_change"]
    trigger = driver.find_element_by_css_selector(jquery_settings["trigger_element_selector"])
    target = driver.find_element_by_css_selector(jquery_settings["target_element_selector"])
    event = jquery_settings["trigger_event"]
    
    # get the original text before interaction
    original_text = target.text

    # pull the trigger...
    if event == "click":
      # click the trigger element
      trigger.click()
    else:
      # mouse over
      ActionChains(driver).move_to_element(trigger).perform() 
      # mouse out, if necessary
      if event == "mouseout":
        # grab some other element
        other_el = driver.find_element_by_tag_name('body')
        ActionChains(driver).move_to_element(other_el).perform() 

    # get the new text after interaction
    new_text = target.text

    assert new_text != original_text

  def test_animation(self, driver, settings):
    """
    Check that the object's position moves when the target event occurs.
    """
    # grab necessary elements for interaction
    jquery_settings = settings["jquery_settings"]["animation"]
    trigger = driver.find_element_by_css_selector(jquery_settings["trigger_element_selector"])
    target = driver.find_element_by_css_selector(jquery_settings["target_element_selector"])
    event = jquery_settings["trigger_event"]

    # get the original position before interaction
    original_left = target.value_of_css_property('left')
    original_top = target.value_of_css_property('top')
    original_right = target.value_of_css_property('right')
    original_bottom = target.value_of_css_property('bottom')

    # pull the trigger...
    if event == "click":
      # click the trigger element
      trigger.click()
    else:
      # mouse over
      ActionChains(driver).move_to_element(trigger).perform() 
      # mouse out, if necessary
      if event == "mouseout":
        # grab some other element
        other_el = driver.find_element_by_tag_name('body')
        ActionChains(driver).move_to_element(other_el).perform() 

    # pause for a second
    ActionChains(driver).pause(1).perform()

    # get the new position after interaction
    new_left = target.value_of_css_property('left')
    new_top = target.value_of_css_property('top')
    new_right = target.value_of_css_property('right')
    new_bottom = target.value_of_css_property('bottom')

    # compare new and original
    l = new_left != original_left
    r = new_right != original_right
    t = new_top != original_top
    b = new_bottom != original_bottom

    # something must have changed
    assert l or r or t or b

