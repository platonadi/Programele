from lxml import html
import requests
import csv

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

zipped = zip(buyers, prices)

with open('student.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(zipped)

print(list(zipped))