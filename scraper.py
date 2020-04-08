import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


def get_operator_list(website):
    r = requests.get(website)
    soup = BeautifulSoup(r.content, "html5lib")
    return soup.select("tr[class*='trn-table__row']")

def Parser(nickname, website):
    operators = get_operator_list(website)
    dataframe = []
    for operator in operators:
        current_page = get_match_list(web + str(i))
        for idx in range(len(current_page)):
            dataframe.append(data_collect(current_page[-(idx+1)]))
            time.sleep(5)
    return dataframe
    #return pd.DataFrame(dataframe, columns=["website", "bedrooms", "toilets",])


if __name__ == "__main__":
    raw_data = get_operator_list("https://r6.tracker.network/profile/pc/Lucky_Invalid/operators")
    print(raw_data)
