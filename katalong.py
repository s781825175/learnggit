from selenium import webdriver

driver = webdriver.Chrome()     # 打开 Chrome 浏览器

# 将刚刚复制的帖在这
driver.get("https://morvanzhou.github.io/tutorials/data-manipulation/scraping/5-01-selenium/")
driver.find_element_by_link_text(u"小练习: 下载美图").click()
driver.find_element_by_link_text(u"下载文件").click()
driver.find_element_by_xpath("//body").click()
driver.find_element_by_link_text(u"高级爬虫: 让 Selenium 控制你的浏览器帮你爬").click()
# 得到网页 html, 还能截图
html = driver.page_source       # get html
driver.get_screenshot_as_file("./img/sreenshot1.png")
driver.close()
