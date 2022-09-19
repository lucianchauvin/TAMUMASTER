import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pyperclip


courses = ['EDCI', 'EHRD', 'ENDG', 'ENDS', 'ENGL', 'ENGR', 'ENST-', 'ENTC', 'ENTO', 'EPFB', 'EPSY', 'ESET', 'ESSM', 'EURO', 'EVEN', 'FILM', 'FINC', 'FIVS', 'FREN', 'FRSC', 'FSCI', 'FSTC', 'FYEX', 'GALV', 'GENE', 'GEOG', 'GEOL', 'GEOP', 'GEOS', 'GERM', 'HBRW', 'HEFB', 'HHUM', 'HISP', 'HIST', 'HLTH', 'HORT',
           'HUMA', 'IBUS', 'IDIS', 'INST-', 'INTS', 'ISEN', 'ISTM', 'ITAL', 'ITDE', 'JAPN', 'JOUR', 'KINE', 'KNFB', 'LAND', 'LBAR', 'LDEV', 'LING', 'LMAS', 'MARA', 'MARB', 'MARE', 'MARR', 'MARS', 'MART', 'MASC', 'MASE', 'MAST', 'MATH', 'MEEN', 'MEFB', 'MEPS', 'METR', 'MGMT', 'MICR', 'MKTG', 'MLSC', 'MMET', 'MODL', 'MSEN', 'MTDE', 'MUSC', 'MUST', 'MXET', 'NAUT', 'NRSC', 'NUEN', 'NURS', 'NUTR', 'NVSC', 'OCEN', 'OCNG', 'PBSI', 'PERF', 'PETE', 'PHIL', 'PHLT', 'PHYS', 'PLPA', 'POLS', 'PORT', 'POSC', 'RDNG', 'RELS', 'RENR', 'RPTS', 'RUSS', 'RWFM', 'SCEN', 'SCMT', 'SCSC', 'SEFB', 'SENG', 'SOCI', 'SOMS', 'SPAN', 'SPED', 'SPMT', 'STAT', 'TCMG', 'TEED', 'TEFB', 'UGST', 'URPN', 'VIBS', 'VIST', 'VLCS', 'VSCS', 'VTPB', 'VTPP', 'WFSC', 'WGST', 'ZOOL']


cookies = {
    'JSESSIONID': '6584F70D553296FECB942A1C57BB8DA2',
    'TS01a9f0c5': '014200a85b7eb5362d53a2021a2472b02bcf5433fe7a892607bcff78cc747a8c9607434025869724e92edbf8af46dddda29bf301f6cad7ed4f1eb7184dd34a783ebe014e23037d8dcc69d1dab8193764b5747f304e',
    'xe_prod_ssb': '!uLAvzDpf1OtbYghxcfM42YaPjNcQdov8XxXnC0SM3iv/orEQV/I4lGwirk8rkkQHaRtqNm3gkfFDz8w=',
    'TS0114ff3e': '014200a85bb133979c6ece85322904fd701afe49816881fc69016503b706eb13743515b21f51dd7c1cc177c212c19b9e547b90789852a058694e8d151447ba06b5167e9d95',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'JSESSIONID=6584F70D553296FECB942A1C57BB8DA2; TS01a9f0c5=014200a85b7eb5362d53a2021a2472b02bcf5433fe7a892607bcff78cc747a8c9607434025869724e92edbf8af46dddda29bf301f6cad7ed4f1eb7184dd34a783ebe014e23037d8dcc69d1dab8193764b5747f304e; xe_prod_ssb=!uLAvzDpf1OtbYghxcfM42YaPjNcQdov8XxXnC0SM3iv/orEQV/I4lGwirk8rkkQHaRtqNm3gkfFDz8w=; TS0114ff3e=014200a85bb133979c6ece85322904fd701afe49816881fc69016503b706eb13743515b21f51dd7c1cc177c212c19b9e547b90789852a058694e8d151447ba06b5167e9d95',
    'Pragma': 'no-cache',
    'Referer': 'https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/classSearch',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Synchronizer-Token': '9673b7fd-b99b-42da-a766-3cc83ee578ad',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}



for x in courses:
    print("cringe")
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.get(
    #     "https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/classSearch")
    # driver.find_element_by_id("classSearch").click()
    # driver.find_element_by_id("s2id_txt_term").click()
    # time.sleep(1)
    # driver.find_element_by_id("202231").click()
    # driver.find_element_by_id("term-go").click()

    # time.sleep(1)
    # driver.find_element_by_id("s2id_txt_subject").click()
    # driver.find_element_by_id("s2id_autogen1").send_keys(x)
    # time.sleep(1)
    # driver.find_element_by_id("s2id_autogen1").send_keys(Keys.ENTER)
    # time.sleep(1)
    
    # driver.find_element_by_id("advanced-search-link").click()
    # time.sleep(1)
    # driver.find_element_by_id("s2id_txt_campus").click()
    # time.sleep(1)
    # driver.find_element_by_id("CS").click()
    # time.sleep(1)
    # driver.find_element_by_id("search-go").click()
    pyperclip.copy(x)
    i = input(x +  " Enter to continue")

    if i == "x":
        continue
    
    params = {
        'txt_subject': x,
        'txt_campus': 'CS',
        'txt_term': '202231',
        'startDatepicker': '',
        'endDatepicker': '',
        'uniqueSessionId': '9h6lf1663537469204',
        'pageOffset': '0',
        'pageMaxSize': '5000',
        'sortColumn': 'subjectDescription',
        'sortDirection': 'asc',
    }


    response = requests.get('https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults',
                            params=params, cookies=cookies, headers=headers)
    print(response.status_code)
    time.sleep(2)

    f = open("outs/" + x + '.txt', 'w')
    f.write(response.text)