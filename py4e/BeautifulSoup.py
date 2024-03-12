# Use words.txt as the file name
# fname = input("Enter file name: ")

# handle = open('cache.txt')
#
# dd = dict()
# for line in handle:
#     if line.startswith('From '):
#         user = line.split()[5][0:2]
#         dd[user] = dd.get(user, 0) + 1
# kl = list(dd.keys())
# kl.sort()
# for k in kl:
#     print(k, dd.get(k))
# import urllib.request
# print(urllib.request.urlopen('http://data.pr4e.org/romeo.txt'))
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors

# 假设这是你的HTML内容
html_content = """
<html>
<head>
<title>Welcome to the comments assignment from www.py4e.com</title>
</head>
<body>
<h1>This file contains the actual data for your assignment - good luck!</h1>

<table border="2">
<tr>
<td>Name</td><td>Comments</td>
</tr>
<tr><td>Muzzammil</td><td><span class="comments">98</span></td></tr>
<tr><td>Faisal</td><td><span class="comments">87</span></td></tr>
<tr><td>Irene</td><td><span class="comments">85</span></td></tr>
<tr><td>Ahoua</td><td><span class="comments">84</span></td></tr>
<tr><td>Morag</td><td><span class="comments">83</span></td></tr>
<tr><td>Brenae</td><td><span class="comments">82</span></td></tr>
<tr><td>Cassie</td><td><span class="comments">81</span></td></tr>
<tr><td>Wasif</td><td><span class="comments">81</span></td></tr>
<tr><td>Nassir</td><td><span class="comments">78</span></td></tr>
<tr><td>Leyla</td><td><span class="comments">78</span></td></tr>
<tr><td>Zakariya</td><td><span class="comments">78</span></td></tr>
<tr><td>Danys</td><td><span class="comments">77</span></td></tr>
<tr><td>Brehme</td><td><span class="comments">75</span></td></tr>
<tr><td>Anum</td><td><span class="comments">73</span></td></tr>
<tr><td>Ragid</td><td><span class="comments">69</span></td></tr>
<tr><td>Maxx</td><td><span class="comments">67</span></td></tr>
<tr><td>Sania</td><td><span class="comments">67</span></td></tr>
<tr><td>Larkin</td><td><span class="comments">62</span></td></tr>
<tr><td>Nasifa</td><td><span class="comments">61</span></td></tr>
<tr><td>Maariyah</td><td><span class="comments">61</span></td></tr>
<tr><td>Derri</td><td><span class="comments">59</span></td></tr>
<tr><td>Laci</td><td><span class="comments">58</span></td></tr>
<tr><td>Palmer</td><td><span class="comments">58</span></td></tr>
<tr><td>Jiao</td><td><span class="comments">52</span></td></tr>
<tr><td>Elisau</td><td><span class="comments">50</span></td></tr>
<tr><td>Damon</td><td><span class="comments">36</span></td></tr>
<tr><td>Kya</td><td><span class="comments">36</span></td></tr>
<tr><td>Emelye</td><td><span class="comments">36</span></td></tr>
<tr><td>Mei</td><td><span class="comments">32</span></td></tr>
<tr><td>Nyah</td><td><span class="comments">30</span></td></tr>
<tr><td>Hazel</td><td><span class="comments">29</span></td></tr>
<tr><td>Aleem</td><td><span class="comments">29</span></td></tr>
<tr><td>Ceira</td><td><span class="comments">27</span></td></tr>
<tr><td>Marrwa</td><td><span class="comments">26</span></td></tr>
<tr><td>Flynn</td><td><span class="comments">25</span></td></tr>
<tr><td>Umar</td><td><span class="comments">22</span></td></tr>
<tr><td>Lianna</td><td><span class="comments">21</span></td></tr>
<tr><td>Henry</td><td><span class="comments">20</span></td></tr>
<tr><td>Zakk</td><td><span class="comments">20</span></td></tr>
<tr><td>Anthony</td><td><span class="comments">18</span></td></tr>
<tr><td>Rhiana</td><td><span class="comments">17</span></td></tr>
<tr><td>Lorraine</td><td><span class="comments">16</span></td></tr>
<tr><td>Coco</td><td><span class="comments">14</span></td></tr>
<tr><td>Keegan</td><td><span class="comments">12</span></td></tr>
<tr><td>Sabrine</td><td><span class="comments">8</span></td></tr>
<tr><td>Leonah</td><td><span class="comments">4</span></td></tr>
<tr><td>Annoushka</td><td><span class="comments">3</span></td></tr>
<tr><td>Mali</td><td><span class="comments">3</span></td></tr>
<tr><td>Aled</td><td><span class="comments">2</span></td></tr>
<tr><td>Chymari</td><td><span class="comments">2</span></td></tr>
</table>
</body>
</html>

"""
soup = BeautifulSoup(html_content, "html.parser")

# 创建一个BeautifulSoup对象
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html_content = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html_content, 'html.parser')

# 使用BeautifulSoup的find_all()函数查找所有的数字
tags = soup('span')
total = 0
for tag in tags:
    # Look at the parts of a tag
    total += int(tag.contents[0])
print(total)
'''
import json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "https://py4e-data.dr-chuck.net/json?"  # input("Enter file name: ")
url = url + urllib.parse.urlencode(dict(key=42, address='University of Wisconsin'))
html = urllib.request.urlopen(url, context=ctx).read()
data = json.loads(html)
print(data.get("results")[0].get("place_id"))
"""
root = ET.fromstring(html)
counts = []
for comment in root.findall('.//comment'):
    count = comment.find('count')
    if count is not None:
        counts.append(int(count.text))
print(sum(counts))

# Retrieve all of the anchor tags
for i in range(7):
    print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[17].get('href')
print(tags[17])
"""
