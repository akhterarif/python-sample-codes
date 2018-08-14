# Get the first page to extract page numbers
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import csv

r = requests.get(
    "https://ngonewsbd.com/wp-content/uploads/2018/01/Bangladeshi-NGO-List.htm")
c = r.content

soup = BeautifulSoup(c, "html.parser")
list_of_data = []
with open('Gobi_ngo_list.csv', 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, 183):
        table_data = soup.find_all("table", {"class": "t" + str(i)})
        for table in table_data:
            tr_data = table.find_all("tr")
            for tr in tr_data:
                data_dict = {}
                p_list = []
                if isinstance(tr, Tag):
                    td_data = tr.find_all("td")
                    for td in td_data:
                        p_data = td.find_all("p")
                        for p in p_data:
                            p_list.append(p.text)
                data_writer.writerow(p_list)
