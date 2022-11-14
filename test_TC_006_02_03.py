from selenium.webdriver.common.by import By


def test_presence_copywriter(driver, correct_login):
    driver.find_element(By.CLASS_NAME, "app_logo").click()
    assert driver.title == "Swag Labs", "NOT FOUNDED"

    a = driver.find_element(By.CLASS_NAME, "footer_copy")
    assert a.text == "© 2022 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy", "copywriter NOT FOUND"

    img = driver.find_element(By.XPATH, '//body/div[@id="root"]/div[@id="page_wrapper"]/footer[1]/img[1]')
    if 'ng-hide' in img.get_attribute('class'):
        print('Image is not visible on screen')
    else:
        print('Image is visible on screen')