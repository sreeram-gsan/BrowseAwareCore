import logging
import requests
import re
from bs4 import BeautifulSoup
import json


class Extract:
    
    
    def __init__(self,extract_data_from_tags):
        self.TAG_RE = re.compile(r"<[^>]+>")
        self.extract_data_from_tags = extract_data_from_tags
        pass

    def remove_HTML_tags(self,text):
        logging.info("Enter remove_HTML_tags")      
        return TAG_RE.sub('', text)


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
        return res

    def get_HTML(self,url):
        logging.info("Enter get_HTML")     
        page = requests.get(url) 
        return BeautifulSoup(page.text, 'html.parser')


    def get_text_from_HTML(self,html):
        
        result = ""
        for tag in extract_data_from_tags:
            result += soup.find(tag)
      
        description = soup3.findAll(attrs={"name":"description"})
        if (len(description) > 0):
            content = clean_up(str(desc[0]['content'].encode('utf-8')))
            if (content is not None):
                final_res+= content
        else:
            logging.debug("Description is Null")
            
        return result


    def get_category(input_url,topic_classification_service_url):      
        logging.info("Enter get_category")      
        extracted_text = extract_text_from_url(input_url)        
        response = json.loads(requests.post(url=topic_classification_service_url,data=extracted_text).text)    
        return response['category']


