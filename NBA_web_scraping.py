# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 09:35:25 2021

@author: Gabriel
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time



play_type_off = ['isolation','hand-off','cut','putbacks','playtype-misc']

play_type_def = ['ball-handler','roll-man','hand-off','putbacks']
for i in play_type_def:


    driver = webdriver.Firefox()

    url = f"https://www.nba.com/stats/teams/{i}/?CF=TEAM_NAME*E*chi&SeasonType=Regular%20Season&TypeGrouping=defensive"

    driver.get(url)

    driver.implicitly_wait(70)

    # select = Select(driver.find_element_by_xpath(r"/html/body/main/div/div/div[2]/div/div/div[1]/div[1]/div/div/label/select"))
    # select.select_by_index(1)
    
    time.sleep(20)
    
    
# select = Select(driver.find_element_by_xpath(r"/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select"))
# select.select_by_index(0)


    src = driver.page_source

    parser = BeautifulSoup(src, "lxml")
    table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})
    headers = table.findAll('th')
    headerlist = [h.text.strip() for h in headers[0:]]
    headerlist = [a for a in headerlist if not "RANK" in a]
    
    rows = table.findAll("tr")[1:]
    player_stats = [[td.getText().strip() for td in rows[i].findAll("td")[0:]] for i in range(len(rows))]
    
    stats = pd.DataFrame(player_stats, columns=headerlist)
    
    pd.DataFrame.to_excel(stats, f"C:\\Users\\gabri\\Desktop\\NBA Data Analytics\\Bulls\\Excels\\2021-22 Season\\Defense\\BullsPlayType_{i}_DEF2021_22.xlsx")

