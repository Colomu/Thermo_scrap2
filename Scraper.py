from ast import Pass
from tkinter import Frame
from tracemalloc import start
from selenium import webdriver
import selenium
import pandas as pd
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep
from typing import List
import os
import urllib
import requests
import wget
import smtplib
import ssl
import creds
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_port = 587
smtp_server = 'smtp.gmail.com'

email_from = 'colomu7@gmail.com'
email_list = 'charlesolomu@yahoo.com', 'colomu7@gmail.com'

pswd = creds.gmail_password

subject = "python email attachments"

from Scraper.constants import BASE_URL
print('start')


class Scraper:
    def __init__(self):
        self.driver_path = "/Users/charlesolomu/Documents/chromedriver"
        #self.service = Service(executable_path=self.driver_path)
        
        self.URL = BASE_URL
        chrome_options = Options()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #self.driver = webdriver.Chrome(self.driver_path, options=chrome_options)
        self.driver.maximize_window()

    def land_first_page(self):
        self.driver.get(self.URL)

    

    def click_element(self, xpath: str = '//a[@href="/uk/en/home/life-science/sequencing.html?icid=HPAB-C3C-sequencing-20150814-us"]'):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        '''fd
        i89\'HJNM  u
        Finds and clicks an element in the website
        parameters
        '''''''
        xpath: str
            The Xpath of the element button

        '''''''''
    
   
        
    def accept_cookies(self, xpath: str = '//a[@class="call"]'):
        '''
        Finds and clicks the "Accept" cookies button.

        parameters
        '''''''
        xpath: str
            The Xpath of the accept cookies button

        '''''''''
    
    
       
        self.driver.switch_to.frame(2) 
        
        
        accept_cookies = self.driver.find_element(By.XPATH, xpath)
        accept_cookies.click()

    def move_to_element(self):
        shop_products = self.driver.find_element(By.XPATH, "(//span[contains(text(),'Shop All Products')])[1]")
        quick_order = self.driver.find_element(By.XPATH, '//span[normalize-space()="Quick Order"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(shop_products)
        time.sleep(2)
        quick_order = self.driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[5]/ul/li[1]/ul/li[3]/a').get_attribute("href")
        self.driver.get(quick_order)
        time.sleep(5)
        catalogue_no = self.driver.find_element(By.XPATH, '//input[@name="items.0.catalogNumber"]')
        catalogue_no.click()
        self.driver.refresh()
        cat_no1 = self.driver.find_element(By.XPATH, '//input[@id="catalogNumber__0"]')
        cat_no1.click()
        time.sleep(2)
        cat_no1.send_keys("MPP100")
        time.sleep(2)
        cat_no2 = self.driver.find_element(By.XPATH, '//input[@id="catalogNumber__1"]')
        cat_no2.click
        time.sleep(2)
        cat_no2.send_keys("60307-312")
        time.sleep(2)
        cat_no3 = self.driver.find_element(By.XPATH, '//input[@id="catalogNumber__2"]')
        cat_no3.click
        time.sleep(2)
        cat_no3.send_keys("28332")
        time.sleep(2)
        qty_cat_no1 = self.driver.find_element(By.XPATH, '//input[@id="quantity__0"]').send_keys(Keys.BACKSPACE)
        qty_cat_no2 = self.driver.find_element(By.XPATH, '//input[@id="quantity__1"]').send_keys(Keys.BACKSPACE)
        qty_cat_no3 = self.driver.find_element(By.XPATH, '//input[@id="quantity__2"]').send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//input[@id="quantity__0"]').send_keys("2")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//input[@id="quantity__1"]').send_keys("4")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//input[@id="quantity__2"]').send_keys("3")
        time.sleep(2)
        add_to_cart = self.driver.find_element(By. XPATH, '//button[@class="qck-order-manualEntryForm__actions--hide-largeMax c-btn c-btn--primary"]')
        add_to_cart.click()
        time.sleep(2)
        checkout = self.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed to checkout']").get_attribute("href")
        self.driver.get(checkout)
       
        

    
    
    

    def primer_order(self):
        pcr = self.driver.find_element(By.XPATH, '(//a[contains(text(),"PCR")])[1]')
        pcr.click()
        design = self.driver.find_element(By.XPATH, '//a[normalize-space()="PCR primers & design"]')
        design.click()
        order_now = self.driver.find_element(By.XPATH, '//span[@class="btn btn-featured"]')
        order_now.click()
        self.driver.implicitly_wait(3)
        
        primer_name = self.driver.find_element(By.XPATH, '(//div[@id="sequence-textbox"])[1]')
        primer_name.send_keys("covid_mRNA")
        time.sleep(2)
        user_name = self.driver.find_element(By.XPATH, "//sequence-textbox[@title='Researcher Name']//div[@id='sequence-textbox']")
        user_name.click()
        time.sleep(2)
        user_name.send_keys("colomu")
        time.sleep(2)
        primer_seq = self.driver.find_element(By.XPATH,'/html/body/div[10]/div/div/project-detail/div/div/oligo-config-detail/div/div[2]/div[1]/div[2]/div[1]/div[1]/sequence-textbox/div/div[2]')
        primer_seq.click()
        time.sleep(2)
        primer_seq.send_keys("ATGCATGC")
       
        
        
class Sequence_scraper(Scraper):


    def get_sequencing(self, xpath: str = '//a[@href="/uk/en/home/life-science/sequencing.html?icid=HPAB-C3C-sequencing-20150814-us"]'):
        sequencing = self.driver.find_element(By.XPATH, xpath)
        sequencing.click()
    
    def sanger_sequencing(self, xpath: str = '(//a[@href="/uk/en/home/life-science/sequencing/sanger-sequencing.html"])[1]'):
        sanger_sequencing = self.driver.find_element(By.XPATH, xpath)
        sanger_sequencing.click()

    def search_equipment(self, xpath: str = '//a[@href="/uk/en/home/life-science/sequencing/sanger-sequencing/sanger-sequencing-technology-accessories.html"]'):  
        equipment = self.driver.find_element(By.XPATH, xpath)
        
        equipment.click()

    def sanger_equipments(self):
        equipments = self.driver.find_elements(By.TAG_NAME, 'tr')

        SeqStudio = []
        SeqStudio_flex = []
        Applied_Biosystem_3500 = []
        Applied_Biosystem_3730 = []

        for equipment in equipments:
            #print(equipment.text)
            #eg = (equipment.find_element (By.XPATH, './td[2]').text)
            #SeqStudio.append(eg)
            #SeqStudio_flex.append(equipment.find_element (By.XPATH, './td[3]').text)
            #Applied_Biosystem_3500.append(equipment.find_element (By.XPATH, './td[4]').text)                #Applied_Biosystem_3730.append(equipment.find_element (By.XPATH, './td[5]').text)
            #print(eg)


            SeqStudio.append(equipment.find_element (By.XPATH, './td[2]').text)
            SeqStudio_flex.append(equipment.find_element (By.XPATH, './td[3]').text)
            Applied_Biosystem_3500.append(equipment.find_element (By.XPATH, './td[4]').text)
            Applied_Biosystem_3730.append(equipment.find_element (By.XPATH, './td[5]').text)

            #df = pd.DataFrame({'SeqStudio': SeqStudio, 'SeqStudio_flex': SeqStudio_flex, 'Applied_Biosystem_3500': Applied_Biosystem_3500, 'Applied_Biosystem_3750': Applied_Biosystem_3730})
            #df.to_csv('Sequencing_Equipments.csv', index=False)

            df = pd.DataFrame({'SeqStudio': SeqStudio, 'SeqStudio_flex': SeqStudio_flex, 'Applied_Biosystem_3500': Applied_Biosystem_3500, 'Applied_Biosystem_3750': Applied_Biosystem_3730})
            df.to_csv('Sequencing_Equipments2.csv')
            print(df)

            #print (equipment.text)
    

class send_mails:

    def send_emails(email_list):

        for person in email_list:

            # make body of email
            body = f""""
            table of sequencing equipments
            pipette images
            AOB
            """

            # make a MIME object to define parts of the email

            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = person
            msg ['Subject'] = subject

            # Attach the body of the message
            msg.attach(MIMEText(body, 'plain'))

        #Define the file to attach

            filename = "Sequencing_Equipments.csv"
            #open file in python as binary
            attachment = open(filename, 'rb') #r for read and b for binary

            # encode as base 64
            attchement_package = MIMEBase('application', 'octet-stream')
            attchement_package.set_payload((attachment).read())
            encoders.encode_base64(attchement_package)
            attchement_package.add_header('content-disposition', "attachment; filename- " + filename)
            msg.attach(attchement_package)

            #cast as string
            text = msg.as_string()

            #connect with the server
            print("connecting to server...")
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls()
            TIE_server.login(email_from, pswd)
            print("Succesfully connected to server")
            print()

            # send emails to "person" as list
            print(f"sending email to: {person}...")
            TIE_server.sendmail(email_from, person, text)
            print(f"email sent to: {person}")
            print()

        TIE_server.quit
        
    send_emails(email_list)

            
    def quit(self):
        close = self.driver.quit()
        close.quit()



class Pipette_scraper(Scraper):
    
    def search_pipettes(self):
        item_search = "pipettes"
        search_bar = self.driver.find_element(By.XPATH, '//input[@name="query"]')
        search_bar.click()
        search_bar.send_keys(item_search)
        search_bar.send_keys(Keys.ENTER)

    def get_images(self):
        images = self.driver.find_elements(By.XPATH, '//img[@class="media-object browse-img-load"]')
        
        src = []
        for image in images:
            src.append(image.get_attribute('src'))  

        for i in range(15):
            urllib.request.urlretrieve(str(src[i]),"pipette_images{}.jpg".format(i))




    
   
   