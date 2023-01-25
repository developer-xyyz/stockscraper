from bs4 import BeautifulSoup
import requests

print("SP Stock checker")
link = input("Enter Link: ")
html_text = requests.get(link).text

soup = BeautifulSoup(html_text, 'lxml')

title = soup.find('title').text

print(title)

content = soup.find('script',id='ProductJson--product-template').text
temp = content.split('variants')
temp2 = temp[1]
temp3 = temp2.split(',')

sizes =[]
stock =[]
for t in temp3:
    firstSeven = t[1:6]
    firstNineteen = t[1:19]
    if(firstSeven == "title"):
        test = t.split(':')
        final = test[1].replace('"',"")
        sizes.append(final)
    if(firstNineteen == "inventory_quantity"):
        test = t.split(":")
        final = test[1].replace('-',"")
        stock.append(final)

i =0
total =0
print("size   stock")
for s in sizes:
    print(s + " : " + stock[i])
    total = total + int(stock[i])
    i = i +1
    
print("total: " + str(total))
