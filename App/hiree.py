# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
from bottle import request, route, run, view

# достает html код по указанной ссылке

local_proc = 0

with open('test.txt', 'r') as file:
    value_d = file.read  #передаем значение файла в переменную
    print(value_d)


def get_html(url, f=True):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    rq = requests.get(url, headers=headers)
    if(f):
        print('Getting HTML-code from ', url)
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
def get_all_resumes_links(query, area):
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url_base = 'https://hh.ru/search/resume?clusters=True'
    url_area = '&area='+area
    url_base2 = '&order_by=relevance&logic=normal&pos=position&exp_period=all_time&no_magic=False&st=resumeSearch'
    url_text = '&text='+query
    url_page = '&page='

    # когда не найдем с помощью bs4 нужный элемент, то выставим его False
    # нужен для остановки цикла перебора всех страниц
    # page_is_not_empty = True

    all_links = []
    for i in range(3):
        url = url_base + url_area+url_base2 + url_text + url_page + str(i)
        # time.sleep(.5)
        html = get_html(url)
        all_links = get_resumes_links(html, all_links)
    return all_links


# функция, которая собирает все ссылки на вакансии на странице поиска
# принимает список, который уже может быть не пустой, возвращает дополненный список
def get_resumes_links(html, all_links):
    # новый объект класса BeutifulSoup
    soup = BeautifulSoup(html, 'lxml')

    links = soup.find_all('a', class_='resume-search-item__name')
    for link in links:
        link_parsed = ("http://hh.ru") + link.get('href')
        all_links.append(link_parsed)
    return all_links


# Функция, которая парсит блок с опытом работы
def parse_exp_in_resume(soup, demanded_exp, procents, position):
    # находим общий опыт работы
    all_exp = soup.find_all('div', class_='resume-block__experience-timeinterval')
    s = soup.find(
        'span', class_='resume-block__title-text resume-block__title-text_sub').get_text()
    if "Опыт работы" not in s:  # если человек вообще не работал
        # print("=========")
        return False
    s = s.split()
    total_exp = 0  # Общий опыт работы в месяцах
    # Считам общий стаж
    if(len(s) == 6):
        total_exp = int(s[2])*12 + int(s[4])
    elif(s[3] == "год" or s[3] == "лет" or s[3] == "года"):
        total_exp = int(s[2])*12
    else:
        total_exp = int(s[2])
    # print("Общий стаж:", total_exp, "месяцев")
    cur_exp = 0  # Опыт на одном из мест
    s *= 0
    # Рассматриваем каждый опыт работы
    good_exp = 0
    cur_positions = soup.find_all(attrs={"data-qa": "resume-block-experience-position"})
    ind = 0
    for pos in cur_positions:
        if position in pos.get_text().lower():
            exp = all_exp[ind]
            # print(exp.get_text())
            # получаем время
            s = exp.get_text().split()
            if(len(s) == 4):
                cur_exp = float(s[0])*12 + float(s[2])
            elif(s[1] == "год" or s[1] == "лет" or s[1] == "года"):
                cur_exp = float(s[0])*12
            else:
                cur_exp = float(s[0])
            # проверяем опыт
            if(cur_exp >= demanded_exp):
                good_exp += cur_exp
        ind += 1
    if(good_exp/total_exp >= procents/100):
        return True
    else:
        return False


def sort_relevant_jobs(keyword):
    with open('good_resumes.txt', 'r', encoding='utf-8') as f:
        data = dict()
        for link in f:
            html = get_html(link, False)
            soup = BeautifulSoup(html, 'lxml')
            jobs = soup.find_all(attrs={"data-qa": "resume-block-experience-position"})
            ans = 0
            for job in jobs:
                if(keyword in job.get_text().lower()):
                    ans += 1
            data[link] = ans
    # open("good_resumes.txt", "w").close()
    with open('good_resumes2.txt', 'w', encoding='utf-8') as f:
        for k in sorted(data, key=data.get, reverse=True):
            f.write(k + ' ' + str(data[k]) + '\n')



def parse_resumes(links):
    # запишем навыки в файл skills_freq
    print("Ищем подходящие резюме...")
    good_resumes = 0
    with open('good_resumes.txt', 'w', encoding='utf-8') as f:
        for link in links:
            html = get_html(link, False)
            soup = BeautifulSoup(html, 'lxml')
            if(parse_exp_in_resume(soup, 24, 60, "менеджер")):
                f.write(link + '\n')
                good_resumes += 1
    print("Найденно", good_resumes, "подходящих резюме.")


if __name__ == '__main__':
    # print("Введите запрос:")
    # query = input().lower().replace(' ', '+')
    query = 'менеджер+по+продажам'
    area = '2'
    # сначала вытащим все ссылки на резюме по данному запросу и региону
    links = get_all_resumes_links(query, area)
    # # теперь распарсим информацию по каждой ссылке, полученной выше
    parse_resumes(links)
    print('Проверено', len(links), 'вакансий.')
    sort_relevant_jobs('менеджер')
