from BrowseAwareCore.data.URLUtility import *

def test_get_category_of_url():   
    uutil = URLUtility()
    uutil.set_topic_classification_url("http://128.199.148.75:8080/classify")
    assert (uutil.get_category_of_url("https://www.theverge.com/") == "News")
