import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from ScreenManager import CheckImage

class GamerBot:

    def __init__(self, options, path):
        self.options = options
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=path)
        self.actions = ActionChains(self.driver)
        self.finder = CheckImage()
        self.buttons = {'mine1.png':'main.png', 'login.png': 'screen.png', 'mining hub button.png':'return menu.png', 'mine2.png':'mining hub.png', 'claim.png':'claim menu.png'}

    def startgame(self):
        self.driver.get("https://play.alienworlds.io/")
        time.sleep(25)
        cords = self.find_button('login.png')
        self.click(cords[0], cords[1])
        time.sleep(5)
        windows = self.driver.window_handles
        print(windows)

    def click(self, cor1, cor2):
        self.actions.move_to_element_with_offset(self.driver.find_element_by_tag_name('html'), cor1, cor2).click().perform()
        #self.actions.move_by_offset(cor1, cor2).click().perform()

    def find_button(self, button):
        self.finder.upload_image(self.buttons[button])
        return self.finder.find_image(button)

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--start-maximized')
    bot = GamerBot(options, 'chromedriver.exe')
    bot.startgame()