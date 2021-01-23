# WebScraper

Title: “Which Price?”
Program: The program is supposed to compare prices of the same item, but from different sellers,
and compare, and provide the output of the cheapest price for the item searched.

Process: The process for this program is that I will talk to my CSCI 101 instructor and seek his
advice on how the program will provide comparisons of different sellers. I may use help from
some of my friends to help debug the program once it is done. I have not yet decided who I will
be specifically collaborating with as I have not talked with anyone yet. I will, however, mention
who I have worked with when submitting my project.

Concerns: Any concerns I have with this project will mainly be being able to write a code in time
without having issues with time management and the code itself will be able to cover the topics
we learned about in 102, like including lists, functions, conditional statements, logical
expressions, etc. The main difficulty will be comparing the different sellers and how the program
will include the sellers in the first place.

A segment of the Code:
for a in soup.find_all('a', href = True, attrs = {'class':'.s-border-bottom'}):
name = a.find('div' , attrs = {'class':'.a-color-base.a-text-normal'})
price = a.find('div', attrs = {'class':'.a-price-fraction, .a-price-whole'})
rating = a.find('div', attrs = {'class':'.aok-align-bottom'})
products_compared.append(name.txt)
prices_of_products.append(price.text)
rates_of_products.append(rating.text)

This part of the code includes a the .findAll method, which is part of a Python package that is meant to
parse HTML and XML documents. It functions by using parsing trees that make it easier to extract data
from websites. Parse trees are a representation of code that show many details of the parser being
implemented. The code is particularly more similar to concrete syntax. The method mentioned above is
used to return the first found match of the particular tag from the web by taking the name the tag as a
string input.

A function used in the code:
df.to_csv('products.csv', index=False, encoding='utf-8')
This part of the code is a function. You may notice how its syntax is different than the ones built in the
original python module. This is because it is a built-in function of a specific library named Pandas. Pandas
is a library that is mainly imported with the intention of performing data analysis and data manipulation.
More specifically, it is used for the extraction of data and then storing it in the desired format. The
“df.to_csv” is a function that will convert a given data frame and will store it as a CSV file. In this case,
the data frame includes the price, rating, and product name in Amazon that the file is storing. So, after
being called, all the products, their prices, and ratings on amazon listed will be compared to each other
and returned in the actual structure of a data frame, with columns, rows, each of them being labeled.

Execution: To execute the program, the user needs to first choose from the given option of which
websites to choose, which is either 0 or 1. Then, the program will ask what price range, from 0 to 300,
and choosing 0 means that the user wants all the ranges. Next, the program will ask for the product name
that the user specifically wants, and the user can put in anything like, laptops, or HP, or iPods. Then the
program will tell the user how many pages of the results were found, and then it will ask the user for a
specific page range, then, the user will give something like 9-11, or 7-8. I would recommend not to do a
page range greater than 5 because when the program scrapes the web, the speed is a little slow. In the end,
a CSV file should be created that is a data frame of the product names and prices, and links, and should be
in a sorted manner.

Reflection: I learned how to extract data from websites using new libraries like bs4, pandas, and
selenium. Using bs4, I was able to extract data from the website and the fact that I needed to extract the
specific “div” class from the website. I imported Pandas to create a new file and be able to write to that
file the new data I extracted from the website. I used Selenium to get the website I needed to extract the
data from. A specific function is the web driver, where it opens the pathway for the executable path in
order to open it in the same file. Problems I encountered were since I was using a Windows 10 PC, it was
harder for the web driver to execute the specific path specified. Another problem was that some websites
require a robot check, and so that was conflicting with the code I wrote for the website because the robot
check was not part of the executable. I think what I would do differently would be that I would have the
user input a website rather than me giving them a website, and tweak the code so it functions according to
the website they input.
