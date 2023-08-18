
e_regex = r'^[\W\.\+\-]+@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$'
p_regex = r'^\+?1?\d{9,15}$'
s_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,15}$'


def check_validity(text, regex):
    if re.search(regex, text):
        return True
    else:
        return False

if __name__ == '__main__':
    print(("valid", "invalid")[check_validity('', email_regex)])
    print(("valid", "invalid")[check_validity('', phone_regex)]) 
    print(("valid", "invalid")[check_validity('', password_regex)])