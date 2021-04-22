import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import captcha

from ScreenManager import CheckImage

class GamerBot:

    def __init__(self, options, path):
        self.options = options
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=path)
        self.actions = ActionChains(self.driver)
        self.finder = CheckImage()
        self.buttons = {'mine1.png':'main.png', 'login.png': 'screen.png', 'mining hub button.png':'return menu.png', 'mine2.png':'mining hub.png', 'claim.png':'claim menu.png'}
        self.mainWindowHandle = ''

    def startgame(self):
        self.driver.get("https://play.alienworlds.io/")
        cords = self.wait_for_find_button('login.png')
        print(cords)
        self.click(cords[0], cords[1])
        self.mainWindowHandle = self.driver.current_window_handle

        print('Input any key')
        input()
        self.main_cycle()

    def main_cycle(self):
        # main
        print('main')
        cords = self.wait_for_find_button('mine1.png')
        self.click_check(cords[0], cords[1], 'mine1.png')
        while True:

            #second mine
            print('mine2')
            cords = self.wait_for_find_button('mine2.png')
            self.click_check(cords[0], cords[1], 'mine2.png')

            #claim
            print('claim')
            cords = self.wait_for_find_button('claim.png')
            self.click_check(cords[0], cords[1], 'claim.png')


            captcha.kok(self.driver)


            time.sleep(220)
            self.driver.switch_to.window(self.mainWindowHandle)
            # return to mining hub
            print('return to mining hub')
            cords = self.wait_for_find_button('mining hub button.png')
            self.click_check(cords[0], cords[1], 'mining hub button.png')

    def wait_for_find_button(self, button):
        while True:
            self.driver.save_screenshot(self.buttons[button])
            cords = self.find_button(button)
            if cords:
                return cords
            time.sleep(1)

    def click(self, cor1, cor2):
        self.actions.move_to_element_with_offset(self.driver.find_element_by_tag_name('html'), cor1, cor2).click().perform()

    def click_check(self, cor1, cor2, button):
        self.actions.move_to_element_with_offset(self.driver.find_element_by_tag_name('html'), cor1, cor2).click().perform()
        while True:
            time.sleep(3)
            self.driver.save_screenshot(self.buttons[button])
            cords = self.find_button(button)
            print(cords)
            if cords:
                self.actions.move_to_element_with_offset(self.driver.find_element_by_tag_name('html'), cor1, cor2).click().perform()
                print('нажал')
            else:
                break

    def find_button(self, button):
        self.finder.upload_image(self.buttons[button])
        return self.finder.find_image(button)

if __name__ == "__main__":
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--window-size=1600,900")
        chromeProfile = "D:\\Projects\\Python\\alienwords\\User Data"
        options.add_argument(f"--user-data-dir={chromeProfile}")
        options.add_argument("--profile-directory=Profile 1")
    except:
        pass

    bot = GamerBot(options, 'D:\\Projects\\Python\\alienwords\\AWCLicker\\chromedriver.exe')
    bot.startgame()
#6LdaB7UUAAAAAD2w3lLYRQJqsoup5BsYXI2ZIpFF
#___grecaptcha_cfg.clients['0']['I']['I']['callback']();