from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


def start_checking(user, password, class_names, when_opens, error=print):
  driver = webdriver.Firefox()
  driver.implicitly_wait(10)  # seconds
  driver.get("https://www.spire.umass.edu/psp/heproda/?cmd=login&languageCd=ENG")
  assert "SPIRE Logon" in driver.title

  username = driver.find_element_by_id("userid")
  username.clear()
  username.send_keys(user)

  pwd = driver.find_element_by_id("pwd")
  pwd.clear()
  pwd.send_keys(password)

  pwd.send_keys(Keys.RETURN)
  assert "Password are invalid." not in driver.page_source

  time.sleep(5)

  driver.switch_to.frame(driver.find_element_by_id("ptifrmtgtframe"))
  select = driver.find_element_by_id('DERIVED_SSS_SCL_SSS_MORE_ACADEMICS')
  driver.find_element_by_xpath(
    "//select[@id='DERIVED_SSS_SCL_SSS_MORE_ACADEMICS']/option[text()='Enrollment: Add']").click()
  driver.find_element_by_id("DERIVED_SSS_SCL_SSS_GO_1").click()
  time.sleep(5)

  # TODO: Enable this if there are multiple term options on SPIRE 'Enrollment: Add' page.
  # driver.find_element_by_css_selector("input[type='radio'][value='1']").click()
  # driver.find_element_by_id("DERIVED_SSS_SCT_SSR_PB_GO").click()

  while True:
    for class_name in class_names:
      img = driver.find_elements_by_xpath(
        "//table[@id='SSR_REGFORM_VW$scroll$0']//a[text()[contains(., '{}')]]/../../../../td[7]/div/div/img".format(
          class_name))
      if len(img) < 1:
        error("no-match", class_name)
        continue
      if len(img) != 1:
        error("multiple-match", class_name)
        continue
      if "Open" in img[0].get_attribute("alt"):
        when_opens(class_name, img[0].find_element_by_xpath("//ancestor::tr"))
    driver.find_element_by_xpath("//span[@title='Delete Selected']/a").click()
    time.sleep(30)

  # Never reaches, but whatever...
  driver.close()


def error(type, message):
  print(type + ": " + message)


def when_open(class_name, tr_element):
  """
  This is called when a class you searched for is open. The check is currenly done every 30 seconds and so this will
  be called every 30 seconds when the class is open. If this method is called, you might want to enroll into the class
  and try and get back to the 'Enrollment: Add' page as it can then continue looking for other classes that might be
  open.

  :param class_name: The name of the class that opened up. This is the same as the name that was passed as program
                     arguments.
  :param tr_element: The element that represents the row for the class that just opened up. You can use this to tick
                     the checkbox and then click on enroll, or just read other info about the class and add events like
                     call/message yourself to notify of this opening.
  """
  print(class_name)


if __name__ == '__main__':
  if len(sys.argv) < 4:
    print("Usage: python3 {} <username> <password> <courses list...>".format(sys.argv[0]))
  else:
    start_checking(sys.argv[1], sys.argv[2], sys.argv[3::], when_open, error)
