from project import website_namehandling, website_urlhandling, username_handling


#=====================
# Website Name Test
#=====================
def test_website_name_number():
    assert website_namehandling("123") == False
def test_website_name_valid():  
    assert website_namehandling("X.com") == True
def test_website_name_empty():
    assert website_namehandling("") == False
def test_website_name_only_special_character():
    assert website_namehandling("@@@@@") == False

#=====================
# Website URL Test
#=====================
def test_website_URL_number():
    assert website_urlhandling("12378") == False
def test_website_URL_domain():
    assert website_urlhandling("google.com") == True
def test_website_URL_https():
    assert website_urlhandling("https://x.com") == True
def test_website_URL_invalid_url():
    assert website_urlhandling("google") == False
def test_website_URL_dot_number():
    assert website_urlhandling("123.234") == False
def test_website_URL_empty():
    assert website_urlhandling("") == False
def test_website_URL_only_special_character():
    assert website_urlhandling("@@@@@") == False

#=====================
# Username Test
#=====================
def test_website_username_number():
    assert username_handling("123") == False
def test_website_username_empty():
    assert username_handling("") == False
def test_website_username_valid_1():
    assert username_handling("Harry@potter") == True
def test_website_username_valid_2():
    assert username_handling("Harry143") == True
def test_website_username_only_special_character():
    assert username_handling("@@@@@") == False