import threading
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
        self.mainbuttons = ['mine1.png', 'mining hub button.png', 'mine2.png', 'claim.png', 'Close.png', 'Close2.png', 'claim_big.png', 'login.png']
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
        while True:

            cords = self.find_any_button()
            if cords:
                print(cords)
                try:
                    self.click(cords[0], cords[1])
                except:
                    pass
            windows = self.driver.window_handles
            if len(windows) > 1:
                try:
                    captcha.kok(self.driver)
                except:
                    self.driver.close()
                time.sleep(2)
                self.driver.switch_to.window(self.mainWindowHandle)
                print(self.mainWindowHandle)
                print(self.driver.current_window_handle)
                time.sleep(7)
            time.sleep(4)


    def wait_for_find_button(self, button):
        while True:
            print('ищу кнопку')
            self.driver.save_screenshot(self.buttons[button])
            cords = self.find_button(button)
            if cords:
                return cords
            time.sleep(1)

    def click(self, cor1, cor2):
        #self.actions.move_by_offset(cor1, cor2).click().perform()
        self.actions.move_to_element_with_offset(self.driver.find_element_by_tag_name('html'), cor1, cor2).click().perform()
        #self.actions.move_to_element(self.driver.find_element_by_tag_name('html')).move_by_offset(cor1, cor2).click().perform()


    def find_any_button(self):
        self.driver.save_screenshot("screen.png")
        for key in self.mainbuttons:
            cords = self.find_button(key)
            if cords:
                return cords
        return ()


    def find_button(self, button):
        self.finder.upload_image("screen.png")
        return self.finder.find_image(button)

if __name__ == "__main__":
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--window-size=1600,900")
        chromeProfile = "D:\\Projects\\Python\\alienwords\\User Data1"
        options.add_argument(f"--user-data-dir={chromeProfile}")
        #options.add_argument("--profile-directory=Profile 1")

    except:
        pass

    bot = GamerBot(options, 'D:\\Projects\\Python\\alienwords\\AWCLicker\\chromedriver.exe')
    bot.startgame()