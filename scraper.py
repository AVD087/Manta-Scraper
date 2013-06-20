# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/adnan/.spyder2/.temp.py
"""

from selenium import webdriver


#scraper configuration
proxyserver = "67.215.228.129" # set your proxy address
proxyport = 7808 #set your proxyport
number_of_pages = 15 # number of pages need to scraped
zipcode = "20176" # insert your target Zipcode 



# proxy configuration
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", proxyserver) 
profile.set_preference("network.proxy.http_port", proxyport) 
profile.update_preferences()
#driver = webdriver.Firefox(profile)
driver = webdriver.Firefox()

#driver = webdriver.Remote( command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)




#parsePage function

def parsePages(n,code):
    pagelink = "http://www.manta.com/mb?pg=%s&search=%s"% (n,code)
    driver.get(pagelink)
    print '***********************'
    print driver.current_url
    print '***********************'

    div=  driver.find_elements_by_xpath('//div[@class = "result-box"]')
    f = open('20176.csv','a')
    for index in range(len(div)):
        
        try:    
            name = div[index].find_element_by_xpath('.//h2/a').text
        except:
            name = ""
    
        try:
            streetAddress = div[index].find_element_by_xpath('.//span[@itemprop = "streetAddress"]').text
        except:
            streetAddress = ""
    
        try:
            locality = div[index].find_element_by_xpath('.//span[@itemprop = "addressLocality"]').text
        except:
            locality =""
        try:
            region = div[index].find_element_by_xpath('.//span[@itemprop = "addressRegion"]').text
        except:
            region = ""

        line = "%s,%s,%s,%s \n" % (name,streetAddress,locality,region)
        f.write(line)
        print line
    f.close()
    
#end of parsePagefunction



for i in range(number_of_pages):
    parsePages(i+1,zipcode)


driver.close()