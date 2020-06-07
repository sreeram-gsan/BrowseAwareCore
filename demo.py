import logging
import BrowseAwareCore.data.URLUtility

logging.basicConfig(filename='demo.log', filemode='w',level=logging.DEBUG)
uutil = URLUtility()
uutil.set_topic_classification_url("http://128.199.148.75:8080/classify")
print (uutil.get_category_of_url("https://www.theverge.com/"))