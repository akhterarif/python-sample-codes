import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import csv
import pandas as pd

import os
import urllib
# import urllib2

csv_name = input("Enter CSV file Name : ")
time = input("Enter time string : ")

df = pd.read_csv("{csv_name}.csv".format(csv_name=str(csv_name)))
resolution = '1500x1500'
ext = '.jpg'
time = str(time)
i = 0
img_data_list = []
csv_file_name = "album_info_{time}.csv".format(time=time)
image_data_header = "image,title,artist,genre\n"
with open(csv_file_name, 'w') as f:
    f.write(image_data_header)

for link in df['name']:
    i = i + 1
    file_name = "image_{time}_{i}.jpg".format(time=time, i=i)
    print(file_name + " Downloading...")
    r = requests.get(link)
    c = r.content

    soup = BeautifulSoup(c, "html.parser")
    image_data = soup.find_all("img", {"class": "we-artwork__image"})

    title_tag = soup.find("span", {"class": "product-header__title"})
    title = title_tag.contents[0] if len(title_tag.contents) else ""

    identity_tag = soup.find("span", {"class": "product-header__identity"})
    identity_anchor = identity_tag.find("a")
    identity = identity_anchor.contents[0] if len(
        identity_anchor.contents) else ""

    genre_tag = soup.find("ul", {"class": "product-header__list"})
    genre_anchor = genre_tag.find("a", {"class": "link link--no-tint"})
    genre = genre_anchor.contents[0] if len(
        genre_anchor.contents) else ""

    img_data = file_name + ',' + title + ',' + identity + ',' + genre + ',' + '\n'
    img_data_list.append(image_data)

    image_link_str = image_data[0]['src']
    splitted_image_link_str_list = image_link_str.split('/')
    splitted_image_link_str_list[-1] = resolution + ext
    res_image_url_str = '/'.join(splitted_image_link_str_list)
    image_file = urllib.request.urlretrieve(
        res_image_url_str, os.path.basename(file_name))

    with open(csv_file_name, 'a+') as f:
        f.write(img_data)

    print(file_name + " Downloaded")
