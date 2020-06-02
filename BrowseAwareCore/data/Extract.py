import logging
import requests
import re
from bs4 import BeautifulSoup
import json


class Extract:
    
    
    def __init__(self,input_url,topic_classification_service_url):
        self.input_url = input_url
        self.topic_classification_service_url = topic_classification_service_url
        pass

    def clean_up(self,text):
        logging.info("Enter clean_up")     
        char_dic = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        temp = []
        res = ""
        temp = text.split(' ')

        for i in temp:
            flag = 0
            for j in str(i):
                if j not in char_dic:
                    flag += 1
            if (flag == 0):
                res += i
            res += " "
        logging.info("Exit clean_up")
        return res

    def extract_text(self):
        logging.info("Enter extract")      
                
        res = requests.get(self.input_url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)

        output = ''
        blacklist = [
	        '[document]',
	        'noscript',
	        'header',
	        'html',
	        'meta',
	        'head', 
	        'input',
	        'script',
	        'style' #More tags needs to be added
            ]

        for t in text:
	        if t.parent.name not in blacklist:
		        output += '{} '.format(t)
        logging.debug("Extracted Text: ")
        logging.debug(output)
        return output

    def get_category_of_url(self):      
        logging.info("Enter get_category_of_url")      
        extracted_text = self.extract_text()
        response = requests.post(url=self.topic_classification_service_url,data=self.clean_up(extracted_text)).json()
        return response['category']




