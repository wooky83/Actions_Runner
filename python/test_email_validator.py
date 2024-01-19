from email_validator import is_valid_email  

def test_email_validator():     
    assert is_valid_email('test@gmail.com') is True   
    # @가 빠져있는 비정상적인 케이스     
    assert is_valid_email('testgmail.com') is False