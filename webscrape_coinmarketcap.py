from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

# Extract the table bodies
tbody = doc.tbody

# Obtain all of table rows
trs = tbody.contents

# Traversing the different levels in the html tags
# Obtaining row data of previous sibling
trs [1].previous_sibling
trs[0].next_siblings

# Converting generator object to a list
list(trs[0].next_siblings)

# Identifying the parent tag
trs[0].parent.name

# Identifying the parent tag
list(trs[0].descendants)
list(trs[0].contents)
list(trs[0].children)

prices = {}

for tr in trs[:10]:
   name, price = tr.contents[2:4]
   fixed_name = name.p.string
   fixed_price = price.a.string

   prices[fixed_name] = fixed_price

print(prices)