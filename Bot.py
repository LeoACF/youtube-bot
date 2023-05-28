# import chromedriver_binary
# from selenium import webdriver
# import time

# class roboYoutube():
# 	def __init__(self):
# 		self.webdriver = webdriver.Chrome()

# 	def busca(self, busca):
# 		url = "https://www.youtube.com/results?search_query=%s" %busca
# 		self.webdriver.get(url)

# Bot = roboYoutube()
# Bot.busca("teste")

import chromedriver_binary
from selenium import webdriver
import time

class roboYoutube():
    def __init__(self):
        self.webdriver = webdriver.Chrome()

    def search_video(self, query):
        self.webdriver.get("https://www.youtube.com")
        search_box = self.webdriver.find_element_by_name("search_query")
        search_box.send_keys(query)
        search_box.submit()
        time.sleep(2)

    def play_video(self, video_index):
        videos = self.webdriver.find_elements_by_css_selector("#video-title")
        if video_index >= len(videos):
            print("Invalid video index")
            return
        video = videos[video_index]
        video.click()
        time.sleep(2)

    def close(self):
        self.webdriver.quit()

# Create an instance of roboYoutube
Bot = roboYoutube()

# Search for a video
Bot.search_video("OpenAI ChatGPT")

# Play the first video
Bot.play_video(0)

# Wait for 10 seconds (you can modify this as needed)
time.sleep(10)

# Close the browser
Bot.close()
