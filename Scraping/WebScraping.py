import urllib.request
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

#file_handler = open('grill-and-bbq.csv', 'w')
file_handler  = io.open('grill-and-bbq.csv', "w", encoding="utf-8")
# put header
file_handler.write("{}\n".format("PAGE|URL|COUNT|INGREDIENT|AMOUNT"))

for j in range(190,348):
    print("Open recipe page #: ",str(j))
    with contextlib.closing(urllib.request.urlopen(mainpage+str(j))) as url:
        htmltext = url.read().decode('utf-8')
    # scrape a list of recipe websites for each page
    results = re.findall(pattern,htmltext)
    for i in range(len(results)):
        # scrape the ingredients per websites from the previous result    
        for i in range(len(results)):
            recipe_url  = re.findall(recipe_pat,results[i])
            with contextlib.closing(urllib.request.urlopen(recipe_url[0])) as recipe_req:
                recipe_html = recipe_req.read().decode('utf-8')
            ingredients = re.findall(ingre_re,recipe_html)
            amount     = re.findall(amt_re,recipe_html)
            # write the results in csv file
            for l in range(len(ingredients)):  
                ingre = ingredients[l].replace('"glosslink">','').replace('</a>','')
                amt = amount[l].replace('"amount">','').replace('</span>','')
                file_handler.write("{}\n".format(str(j)+"|"+recipe_url[0]+"|"+str(len(amount))+"|"+amt+"|"+ingre))