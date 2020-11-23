import re
def regex_price(text):
    return re.search("\d{1}(\.\d{1,4})?", text).group()