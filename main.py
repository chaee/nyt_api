# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from pynytimes import NYTAPI
import api_key

api_key = api_key.key

nyt = NYTAPI(api_key, parse_dates=True)

articles = nyt.article_search(query = "Elon Musk", results = 20)

#Assign the data in the first item of articles to a variable

article = articles[0].copy()

#Recommended deleting the multimedia key to reduce clutter in the data

del article["multimedia"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
