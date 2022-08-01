from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

url = f"https://www.goodreads.com/book/show/37976541-bad-blood"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(id= "bookReviews")

book_rating = doc.find_all(class_="reviewHeader uitext stacked") # Obtain the reviewer's name, rating and review date

username = []
ratings = []
review_date = []

for rating in book_rating:
    try:
        user = rating.find(class_="user").get_text()
        rating_stars = rating.find(class_="staticStar p10").get_text()
        date = rating.find(class_="reviewDate createdAt right").get_text()

        username.append(user)
        ratings.append(rating_stars)
        review_date.append(date)
    except:
        pass

book_review = doc.find_all(class_="reviewText stacked") # Obtain the review text

reviews = []

for review in book_review:
    try:
        full_review = review.find(style="display:none").get_text()
        reviews.append(full_review)
    except:
        full_review = review.find(class_="readable").get_text()
        reviews.append(full_review)

goodreads_reviews = pd.DataFrame(np.column_stack([username,ratings,review_date,reviews]),columns=['username','ratings','review_date','reviews']) #appending all the information into a dataframe

print(goodreads_reviews)
