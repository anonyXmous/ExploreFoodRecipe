# ExploreFoodRecipe
Collaboration project with Chisoo Kim and <insert more data scientists here 4/4/2017> to explore new recipes using data science.  This project focuses on bbq-and-grilling because it is simple to prepare but can be extended to other types of food preparations.  Website used is bigoven.com and no permission was asked from the website owner so data is used for personal use and not for public usage.

Python scripts:
getUrl.py - For extracting the url of recipes and dump into a csv file for reading in next step  and getRe.py - For extracting the ingredients and amount  Main Author: Jun
Grill-and-bbq-Data-Cleaning.ipynb - For data cleaning, mungling, extracting recipe name and recipe id including stemming of ingredients Main Author: Chisoo
Stemming.ipynb and MostCommon.ipynb - To generate new recipes based on similarities of ingredients per recipes and listing out most common and least common ingredients Main Author: Jun

Datasets:  
 1) RECIPE.csv   (PAGE|URL|COUNT|INGREDIENT|AMOUNT):  
 Page is page number in the website where recipe is taken
 URL is the recipe url
 COUNT not used since data is not consistently correct
 INGREDIENT meat/condiment/veggies used in the recipe
 AMOUNT quntity/wt/measurement of ingredient
 2) Ingredients.csv(dish_id|amount|ingredient)
 

