# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import openpyxl


# достает html код по указанной ссылке
def get_html(url):      
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    rq = requests.get(url, headers=headers)
    print('Gettin HTML-code from ', url)
    return rq.text


# проверяет, есть ли на странице ссылки на вакансии
def is_empty(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('resume-serp_block-result-action')
    if links == []:
        return True
    else:
        return False


# функция, которая для данного запроса и региона ищет все страницы с результатами поиска и набирает большой список со всеми ссылками на вакансии
# возвращает список ссылок по запросу query в регионе с кодом area
def get_all_offers_links(query, area):
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url_base = 'https://spb.hh.ru/search/resume?clusters=True&area=2&order_by=relevance&logic=normal&pos=position&exp_period=all_time&no_magic=False&st=resumeSearch'
    url_text = '&text='+query
    #url_area = '&area='+area
    url_page = '&page='

    # когда не найдем с помощью bs4 нужный элемент, то выставим его False
    # нужен для остановки цикла перебора всех страниц
    page_is_not_empty = True

    all_links = []
    page = 1

    for i in range(3):
        url = url_base + url_text + url_page + str(i)
        time.sleep(.5)
        html = get_html(url)
        all_links = get_offers_links(html, all_links)
        """if not is_empty(html):
            all_links = get_offers_links(html, all_links)
            
            page += 1
        else:
            page_is_not_empty = False
        """
    return all_links




"""
Здесь мы выдаем ссылки на резюме
"""
# функция, которая собирает все ссылки на вакансии на странице поиска
# принимает список, который уже может быть не пустой, возвращает дополненный список
def get_offers_links(html, all_links):
    # новый объект класса BeutifulSoup
    soup = BeautifulSoup(html, 'lxml')

    links = soup.find_all('a', class_='resume-search-item__name')
    for link in links:
        link_parsed = ("http://spb.hh.ru") + link.get('href')
        all_links.append(link_parsed)
    return all_links




# функция, которая парсит блок с ключевыми навыками и возвращает дополненный словарь, который ей дали на входе
def parse_skills_in_offer(soup, skill_dict):   ##############################################################################/
    # находим блок с ключевыми навыками на странице
    key_skills = soup.find_all('div', class_='resume-block-experience')
    #exper = soup.find("лет")
   # soup.select('.resume-block__title-text_sub')
    # добавляем текст навыков в словарь
    print(key_skills)
    for skill in key_skills:
        if skill.get_text().lower() in skill_dict:
            skill_dict[skill.get_text().lower()] += 1
        else:
            skill_dict[skill.get_text().lower()] = 1

    return skill_dict



# функция, которая парсит блок с описанием вакансии и возвращает дополненный словарь, который ей дали на входе

if __name__ == '__main__':
    query = 'менеджер+по+продажам'
    area = '2'
    # сначала вытащим все ссылки на вакансии по данному запросу и региону
    links = get_all_offers_links(query, area)
    # теперь распарсим информацию по каждой ссылке, полученной выше
    #parse_offers(links)

    print('Проверено ',len(links), ' вакансий.')
