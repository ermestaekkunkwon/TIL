"""
https://www.dhlottery.co.kr/common.do
?
method=getLottoNumber
&
drwNo=837
"""

import requests


URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

requests.get(URL)

got = requests.get(URL)

print(got)