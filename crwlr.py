# example: https://docs.python-guide.org/scenarios/scrape/
from lxml import html
import requests

#get page:
response = requests.get('https://www.yad2.co.il/s/c/hecmjl', 
     headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0"})

if(response.status_code == 200):
     tree = html.fromstring(response.content)

     # get price (using xpath):
     # I need this, but its not working:
     the_correct_xpath_to_the_prices = tree.xpath('/html/body/div[4]/div[2]/div/main/div[1]/div[3]/div[5]/div/div[1]/div/div/div[2]/div[2]/div/strong')
     price_wrap_div = tree.xpath("//div[@class='wrapper_content']")
     print(price_wrap_div)
     print(the_correct_xpath_to_the_prices)
     # this is the only working:
     the_only_working_xpath = tree.xpath('/html/body/div[3]/div[2]/div/main/div')
     print(the_only_working_xpath)