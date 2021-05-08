from anticaptchaofficial.recaptchav2proxyless import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('token.txt') as f:
    token = f.read()

def kok(driver, startflag):
    flag = True
    while flag:
        windows = driver.window_handles
        for window in windows:
            driver.switch_to.window(window)
            element_err = driver.find_elements_by_xpath('//div[@id="cf-error-details"]')
            element = driver.find_elements_by_xpath('//*[@id="g-recaptcha-response"]')
            if element:
                break
            if element_err:
                driver.get("https://all-access.wax.io/cloud-wallet/signing/")
                time.sleep(2)

        for window in windows:
            driver.switch_to.window(window)
            element = driver.find_elements_by_xpath('//*[@id="g-recaptcha-response"]')
            if element:
                print(driver.current_url)
                kekw = getKey(driver.current_url)
                while kekw == 0:
                    kekw = getKey(driver.current_url)
                    #raise Exception('3228')
                print('found kok')

                lol = "___grecaptcha_cfg.clients['0']['B']['B']['callback']('"+kekw+"');"
                print(lol)
                driver.execute_script(lol)
                if not startflag:
                    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button button-secondary button-large text-1-5rem text-bold mx-1']")))
                    element.click()

                flag = False

                break
            time.sleep(0.5)



def getKey(url):

    from selenium.webdriver.support.wait import WebDriverWait

    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key(token)
    solver.set_website_url(url)
    solver.set_website_key("6LdaB7UUAAAAAD2w3lLYRQJqsoup5BsYXI2ZIpFF")
    # set optional custom parameter which Google made for their search page Recaptcha v2
    # solver.set_data_s('"data-s" token from Google Search results "protection"')
    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        print("g-response: " + g_response)
        return g_response
    else:
        print("task finished with error " + solver.error_code)
        return 0