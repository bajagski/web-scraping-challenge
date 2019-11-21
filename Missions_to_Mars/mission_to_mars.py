#!/usr/bin/env python
# coding: utf-8


#dependencies
import pandas as pd
import os
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import time


# In[70]:


#browser = webdriver.Chrome(executable_path=r'C:\Users\13124\Documents\web-scraping-challengechromedriver.exe')
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)


# In[71]:


#Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[72]:


#Use Beautiful soup
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[73]:


#collect the latest News Title and Paragraph Text and Assign the text to variables that you can reference later.
news_title = soup.find("div",class_="content_title").text
print(news_title)
news_p = soup.find("div", class_="article_teaser_body").text
print(news_p)


#Use splinter to navigate the site and 
#find the image url for the current Featured Mars Image and 
#assign the url string to a variable called featured_image_url

image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)


# Use BeautifulSoup
image_html = browser.html
soup = BeautifulSoup(image_html, 'html.parser')


featured_image = soup.find('img', class_ = 'thumb')['src']
featured_image_url = "https://www.jpl.nasa.gov" + featured_image
print(featured_image_url)


# Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. 
mars_weather_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(mars_weather_url)

weather_html = browser.html
soup = BeautifulSoup(weather_html, 'html.parser')



# Save the tweet text for the weather report as a variable called mars_weather.
mars_weather = soup.find("p", class_= "TweetTextSize").text
print(mars_weather)



# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet 
# including Diameter, Mass, etc. 
mars_facts_url = "https://space-facts.com/mars/"

mars_table = pd.read_html(mars_facts_url)


df = mars_table[0]
df.columns = ['description', 'values']
df.head(10)


# Use Pandas to convert the data to a HTML table string.
mars_facts = df.to_html()
print(mars_facts)


# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, 
# and the Hemisphere title containing the hemisphere name. 
# Use a Python dictionary to store the data using the keys img_url and title.
# Append the dictionary with the image url string and the hemisphere title to a list. 
# This list will contain one dictionary for each hemisphere.


mars_hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemi_url)

browser.click_link_by_partial_text("Cerberus")
time.sleep(3)
mars_hemi_html = browser.html
soup = BeautifulSoup(mars_hemi_html, 'html.parser')

cerberus_image = soup.find('a', target = "_blank")['href']
cerberus_title = soup.find('h2', class_ = "title").text


mars_hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemi_url)


browser.click_link_by_partial_text("Schiaparelli")
time.sleep(3)
mars_hemi_html = browser.html
soup = BeautifulSoup(mars_hemi_html, 'html.parser')

schiaparelli_image = soup.find('a', target = "_blank")['href']
schiaparelli_title = soup.find('h2', class_ = "title").text


mars_hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemi_url)


browser.click_link_by_partial_text("Syrtis")
time.sleep(3)
mars_hemi_html = browser.html
soup = BeautifulSoup(mars_hemi_html, 'html.parser')

syrtis_image = soup.find('a', target = "_blank")['href']
syrtis_title = soup.find('h2', class_ = "title").text


mars_hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemi_url)



browser.click_link_by_partial_text("Valles")
time.sleep(3)
mars_hemi_html = browser.html
soup = BeautifulSoup(mars_hemi_html, 'html.parser')

valles_image = soup.find('a', target = "_blank")['href']
valles_title = soup.find('h2', class_ = "title").text


mars_hemi = [{"image_url" : cerberus_image, "title": cerberus_title}, 
             {"image_url": schiaparelli_image, "title": schiaparelli_title},
            {"image_url": syrtis_image, "title": syrtis_title},
            {"image_url": valles_image, "title": valles_title}]

mars_hemi

