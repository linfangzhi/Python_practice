import requests
import json
from bs4 import BeautifulSoup



a = requests.get('https://job.bytedance.com/api/recruitment/position/list/?type=1&summary_id=&sequence=&city=128,45&q1=%E6%95%B0%E6%8D%AE&name=&limit=10&offset=0&position_type=&_signature=hP4OIAAgEAtjifYm2VUtuIT-DjAANr-')
#a.encoding = 'unicode_escape'
data = a.text
print(data)
dict_data = dict(data)
print(dict_data)
print(dict_data['positions'])






