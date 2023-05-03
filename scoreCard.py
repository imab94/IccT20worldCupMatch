import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import numpy as np
import re
import requests
# import html5lib
""""
India vs Netherlands world cup score card 2022..
"""
fetch_score = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/india-vs-netherlands-23rd-match-group-2-1298157/match-overs-comparison"

# fetch_score = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/england-vs-india-2nd-semi-final-1298178/match-overs-comparison"

over = 1

india = []
Netherland = []

# def fetch_score_from_website(url):
resp = requests.get(fetch_score)
soup = BeautifulSoup(resp.content,'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib
# print(soup.prettify())
# script_tag = soup.find('div',attrs={"class":"ds-border ds-border-line"})
# inside_script_tag = script_tag.find('tbody')
# inside_script_tag1 = inside_script_tag.find_all('td',attrs={"class":"ds-min-w-max !ds-align-top"})
# data = inside_script_tag1[0].find_all_next("span")
# print(inside_script_tag1[1])
# for data in range(len(inside_script_tag1)):
#     data_in_over.append(inside_script_tag1[data].text)
# print(data_in_over)
span_tag = soup.findAll("span",attrs={"class":"ds-text-tight-s ds-font-regular ds-ml-1 ds-text-typo-mid3"})
# print(span_tag)

for row in span_tag:
    row = str(row)
    temp = re.findall(r"\d+ runs",row)
    # print(temp)
    if over % 2 != 0:
        india.extend(temp)
    if over % 2 == 0:
        Netherland.extend(temp)
    over += 1

# print(india)
# print(Netherland)
INDIA = [int(i.split()[0]) for i in india]
NETHERLAND = [int(i.split()[0]) for i in Netherland]
# print(INDIA)
# print(NEITHERLAND)
X = list(map(str,range(1,21))) # overs

# print(X)
Y = list(range(0,40,2)) # RUNS per overs
# print(Y)
X_axis = np.arange(len(X))
Y_axis = np.arange(len(Y))

# fig, ax = plt.subplots()

plt.bar(X_axis-0.12,INDIA,width=0.25, label = 'INDIA')
plt.bar(Y_axis+0.12, NETHERLAND, width=0.25, label = 'NEITHERLAND')

plt.xlabel("OVERS")
plt.ylabel("RUNS")
plt.xticks(X_axis,X)

plt.title("MATCH SCORECARD T20 WORLD CUP ")
plt.legend()
plt.show()



