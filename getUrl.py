import urllib.request
import urllib.request
from urllib.error import URLError, HTTPError
import re
import io
import contextlib

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

#file_handler = open('grill-and-bbq-url.csv', 'w')
file_handler  = io.open('grill-and-bbq-url.csv', "w", encoding="utf-8")
file_error = open('error.csv', 'w')

# put header
file_handler.write("{}\n".format("PAGE|URL|COUNT|AMOUNT|INGREDIENT"))

for j in range(190,238):
    #print("Open recipe page #: ",str(j))
    try:
        with contextlib.closing(urllib.request.urlopen(mainpage+str(j))) as url:
            htmltext = url.read().decode('utf-8')
    except HTTPError as e:
        print("HTTPError on page: "+ str(j)) 
        file_error.write("{}\n".format("HTTPError = " + str(e.code)))
        break
    except URLError as e:
        print("URLError on page: "+ str(j)) 
        file_error.write("{}\n".format("URLError = " + str(e.reason)))
        break       
    else:
        # scrape a list of recipe websites for each page
        #print(htmltext)
        results = re.findall(pattern,htmltext)
        #file_handler.write("{}\n".format(htmltext))
        for i in range(len(results)):
            recipe_url  = re.findall(recipe_pat,results[i])
            file_handler.write("{}\n".format(str(j)+"|"+recipe_url[0]))
        print("print page #: ",str(j))    
    
        