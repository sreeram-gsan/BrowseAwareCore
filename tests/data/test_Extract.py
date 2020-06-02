from BrowseAwareCore.data.Extract import Extract

def test_get_category_of_url():
    extract = Extract("https://www.theverge.com/","http://128.199.148.75:8080/classify")    
    assert (extract.get_category_of_url() == "News")
