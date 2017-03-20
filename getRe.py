import urllib.request
import re
import io
import contextlib
import csv

mainpage = "https://www.bigoven.com/recipes/main-dish/grill-and-bbq/page/"

# look for pattern that starts with tag data-url on the mainpage
# thanks to http://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
regex = 'data\-url\=\"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\"'
pattern = re.compile(regex)

# pattern for webpage for recipes
recipe_re = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
recipe_pat = re.compile(recipe_re)

ingre_re = r'"glosslink">+.*</a>+'
amt_re   =  r'"amount">+.*</span>+'

file_handler  = io.open('grill-and-bbq.csv', "w", encoding="utf-8")
file_error = open('error.csv', 'w')
# put header
file_handler.write("{}\n".format("PAGE|URL|COUNT|AMOUNT|INGREDIENT"))

with open('grill-and-bbq-url.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='|')
    for row in readCSV:        
        try:
            with contextlib.closing(urllib.request.urlopen(row[1])) as recipe_req:
                recipe_html = recipe_req.read().decode('utf-8')
        except HTTPError as e:
            print("HTTPError on page: "+ str(j)) 
            file_error.write("{}\n".format("HTTPError = " + str(e.code)))
            break
        except URLError as e:
            print("URLError on page: "+ str(j)) 
            file_error.write("{}\n".format("URLError = " + str(e.reason)))
            break       
        else:
            # scrape the ingredients per websites from the previous result 
            ingredients = re.findall(ingre_re,recipe_html)
            amount     = re.findall(amt_re,recipe_html)
            # write to csv file
            for l in range(len(ingredients)):
                ingre = ingredients[l].replace('"glosslink">','').replace('</a>','')
                amt = amount[l].replace('"amount">','').replace('</span>','')
                file_handler.write("{}\n".format(row[0]+"|"+row[1]+"|"+str(len(amount))+"|"+amt+"|"+ingre))
        print("Open recipe page: " + row[0] + " is done.")

